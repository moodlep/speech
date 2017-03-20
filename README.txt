Notes:

1. export GOOGLE_APPLICATION_CREDENTIALS=xxxxx/git_repos/auth_keys/CloudVisionPrj-3b7fedb71edc.json

 2. Updates performed:

pip install --upgrade google-cloud-speech

pip install --upgrade google-api-python-client

pip install --upgrade google-cloud-language

3. ffmpeg used to extract sound from ML intro video was not so successful.
The conversion worked but the quality was not good in flac format and did not translate well.

Sample commands for ffmpeg below:

To aac format:
ffmpeg -i Model_Representation.mp4 -vn -acodec copy output.aac

Or just get 45 seconds starting from this time stamp
ffmpeg -i Model_Representation.mp4 -ss 00:00:00 -t 00:00:45.0 -vn -acodec copy output.aac

aac not accepted, trying wav - smaller sample:
ffmpeg -i Model_Representation.mp4 -ss 00:00:00 -t 00:00:10.0 -vn  output.wav

Creating flac files (Remember to change the encoding to match FLAC in the json request!):

ffmpeg -i Model_Representation.mp4 -ss 00:00:00 -t 00:00:10.0 -acodec flac -bits_per_raw_sample 16 -ar 16000 output_16000.flac
Removing the extra channel:
ffmpeg -i output_16000.flac -ac 1 mono.flac

4. Downloaded audacity to create flac files directly from laptop!

Set PCM 16-bit
Mono
16000Hz

Seems to work ok without any further conversion required in ffmpeg.

see positive.flac and negative.flac

5. Hit a snag with nlp - some parts are still in alpha. Need to sort out client cloud sdk.
 Reverting to python 2.7 and updated all google sdks on 2.7.
 Testing from the command line and nlp snippet works.

6. APIs that may be interesting to call
Arxiv: https://arxiv.org/help/api/user-manual#Architecture
http://export.arxiv.org/api/query?search_query=ti:"reinforcement learning"&sortBy=lastUpdatedDate&sortOrder=descending&max_results=10
