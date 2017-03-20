"""Google Cloud Speech API sample application using the REST API for batch
processing.
Example usage: python transcribe.py resources/audio.raw
"""

# [START import_libraries]
import argparse
import base64
import json

import googleapiclient.discovery
from oauth2client.client import GoogleCredentials
from google.cloud import language

# [END import_libraries]


# [START authenticating]
# Application default credentials provided by env variable
# GOOGLE_APPLICATION_CREDENTIALS
def get_speech_service():
    DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
    credentials = GoogleCredentials.from_stream('/Users/perusha/git_repos/auth_keys/CloudVisionPrj-3b7fedb71edc.json')
    return googleapiclient.discovery.build('speech', 'v1beta1', credentials=credentials, discoveryServiceUrl=DISCOVERY_URL)
# [END authenticating]

# [END sentiment_tutorial_import]

def nlp_text(text):
    #NLP: Instantiates a client
    language_client = language.Client()

    # The text to analyze
    document = language_client.document_from_text(text)

    # Detects the sentiment of the text
    sentiment = document.analyze_sentiment().sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


def print_result(annotations):
    score = annotations.sentiment.score
    magnitude = annotations.sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0

    print('Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    language_client = language.Client()

    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        document = language_client.document_from_html(review_file.read())

        # Detects sentiment in the document.
        annotations = document.annotate_text(include_sentiment=True,
                                             include_syntax=False,
                                             include_entities=False)

        # Print the results
        print_result(annotations)


def main(speech_file):
    """Transcribe the given audio file.
    Args:
        speech_file: the name of the audio file.
    """
    # [START construct_request]
    with open(speech_file, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the JSON
        # request.
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'FLAC',  # raw 16-bit signed LE samples
                'sampleRate': 16000,  # 16 khz
                # See http://g.co/cloud/speech/docs/languages for a list of
                # supported languages.
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    # [END construct_request]
    # [START send_request]
    response = service_request.execute()

    # First print the raw json response
    # print(json.dumps(response, indent=2))

    # Now print the actual transcriptions
    for result in response.get('results', []):
        print('Result:')
        for alternative in result['alternatives']:
            print(u'  Alternative: {}'.format(alternative['transcript']))
            nlp_text(alternative['transcript'])
    # [END send_request]


# [START run_application]
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
    main(args.speech_file)
    # [END run_application]