Open Issues:

1. Followed sample here https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/speech/api-client but authentication did nto work.
Used CloudVision project credentials for service account and discovery code. That works ok but need to figure out why the new code is out.

ran:
pip install --upgrade google-cloud-speech   from   https://cloud.google.com/speech/docs/reference/libraries#client-libraries-install-python
which did something but was incomplete.

then tried:
export GOOGLE_APPLICATION_CREDENTIALS=/Users/perusha/git_repos/auth_keys/CloudVisionPrj-3b7fedb71edc.json


 2. Two updates performed:

pip install --upgrade google-cloud-speech
no effect

pip install --upgrade google-api-python-client
this upgraded the client and code sample was ok after this.

3. ffmpeg used to extract sound from ML intro video:

ffmpeg -i Model_Representation.mp4 -vn -acodec copy output.aac

Or just get 45 seconds starting from this time stamp
ffmpeg -i Model_Representation.mp4 -ss 00:00:00 -t 00:00:45.0 -vn -acodec copy output.aac

aac not accepted, trying wav - smaller sample
ffmpeg -i Model_Representation.mp4 -ss 00:00:00 -t 00:00:10.0 -vn  output.wav