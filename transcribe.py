import json
from pytube import YouTube
import pytube
import boto3
import re


def lambda_handler(event, context):
    
    transcribe_input_bucket = 'mankoos-transcribe-input'
    transcribe_output_bucket = 'mankoos-transcribe-output'
    
    youtubeurl = event['youtubeurl']

    # Extract Video id from youtube url

    video_id = 'null_video_id'
    for argval in youtubeurl.split('?')[1].split('&'):
        print(argval)
        arg=argval.split('=')[0]
        val=argval.split('=')[1]
        if arg == 'v':
            video_id = val
            print('Video id is: ' + video_id)
            break


    yt = YouTube(youtubeurl)
    
    print("Downloading File...")
    
    downloaded_file = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first().download(output_path='/tmp', filename=video_id)
    print("Download complete.")
    # downloaded_file = "C:\\Users\\sumee\\Google Drive\\github\\youtube-analytics\\The Chainsmokers - Closer ft Halsey (Official Lyric Video).mp4"
    filename = downloaded_file.split('/')[-1]
    
    # Clean filename so as to be acceptable by aws transcribe
    filename = re.sub(r'([^.0-9a-zA-Z._-])', "_", filename)
    s3filekey = filename
    
    
    # Upload to S3
    
    print("Uploading file to S3...")
    
    content = open(downloaded_file, 'rb')
    s3 = boto3.client('s3')
    s3.put_object(
       Bucket=transcribe_input_bucket, 
       Key=s3filekey, 
       Body=content
    )
    
    print("Upload complete.")
    # Get URL for the file uploaded to s3
    object_url = "https://s3.amazonaws.com/{0}/{1}".format(transcribe_input_bucket, s3filekey)
    # print(object_url)
    
    # Create transcribe job
    
    print("Starting a transcribe job...")
    
    transcribe = boto3.client('transcribe')
    response = transcribe.start_transcription_job(
        TranscriptionJobName=filename,
        LanguageCode='en-US',
        MediaFormat='mp4',
        Media={
            'MediaFileUri': object_url
        },
        OutputBucketName=transcribe_output_bucket,
        Settings={
            'ShowSpeakerLabels': False,
            'ChannelIdentification': False
        }
    )
    
    print("Transcribe job started.")
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

event = '{ "youtubeurl" : "https://www.youtube.com/watch?v=kJQP7kiw5Fk" }'
context = ''

lambda_handler(event, context)