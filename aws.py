import boto3
import os

# AWS Access Key ID and Secret Access Key
access_key_id = 'AKIAXYKJRRBQSNB7NKG7'
secret_access_key = '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'

# Function to upload image to S3
def upload_data_to_s3(file_path,object_name=None):
    bucket_name = 'story21'
    if object_name is None:
        object_name = file_path

    # Create S3 client with explicit access keys
    s3_client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    try:
        # Upload the file
        response = s3_client.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        print(e)
        return False
    return True

upload_data_to_s3("output/image/0.png",object_name=None)


def download_data_from_s3(object_name, destination_path):
    bucket_name = 'story21'
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    s3_client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    try:
        # Download the image
        s3_client.download_file(bucket_name, object_name, destination_path)
    except Exception as e:
        print(e)
        return False
    return True


import boto3
import os


    # AWS credentials
    


def text_to_speech(text, lang, output, output_format='mp3'):
    language = {
    'Arabic': 'arb',
    'Arabic (Gulf)': 'ar-AE',
    'Catalan': 'ca-ES',
    'Chinese (Cantonese)': 'yue-CN',
    'Chinese (Mandarin)': 'cmn-CN',
    'Danish': 'da-DK',
    'Dutch (Belgian)': 'nl-BE',
    'Dutch': 'nl-NL',
    'English (Australian)': 'en-AU',
    'English (British)': 'en-GB',
    'English (Indian)': 'en-IN',
    'English (New Zealand)': 'en-NZ',
    'English (South African)': 'en-ZA',
    'English (US)': 'en-US',
    'English (Welsh)': 'en-GB-WLS',
    'Finnish': 'fi-FI',
    'French': 'fr-FR',
    'French (Belgian)': 'fr-BE',
    'French (Canadian)': 'fr-CA',
    'German': 'de-DE',
    'German (Austrian)': 'de-AT',
    'Icelandic': 'is-IS',
    'Italian': 'it-IT',
    'Japanese': 'ja-JP',
    'Korean': 'ko-KR',
    'Norwegian': 'nb-NO',
    'Polish': 'pl-PL',
    'Portuguese (Brazilian)': 'pt-BR',
    'Portuguese (European)': 'pt-PT',
    'Romanian': 'ro-RO',
    'Russian': 'ru-RU',
    'Spanish (European)': 'es-ES',
    'Spanish (Mexican)': 'es-MX',
    'Spanish (US)': 'es-US',
    'Swedish': 'sv-SE',
    'Turkish': 'tr-TR',
    'Welsh': 'cy-GB'}



    polly_client = boto3.client('polly', region_name='us-east-1',
                                aws_access_key_id = 'AKIAXYKJRRBQY2MQLNAD',
                                aws_secret_access_key = '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')

    # Get the list of available voices
    response = polly_client.describe_voices(LanguageCode=language[lang])  
    print(language[lang])

    voices = response['Voices']
    z=0
     # Iterate over voices to find a suitable voice
    for voice in voices:
        if 'neural' in voice["SupportedEngines"]:
            voice_id2 = voice["Id"]
            print(voice_id2)
            z=1
            break
        else:
            voice_id2 = voice["Id"]
            print(voice_id2)

    try:
        # Request the text-to-speech conversion
        if z==1:  # Check if voice_id2 is assigned a value
            response = polly_client.synthesize_speech(
                Text=text,
                VoiceId=voice_id2,
                OutputFormat=output_format,
                Engine="neural"
            )
        else:
            response = polly_client.synthesize_speech(
                Text=text,
                VoiceId=voice_id2,
                OutputFormat=output_format,
                Engine="standard"
            )
    except Exception as e:
        print(f'Error synthesizing speech: {e}')
        return

    # Save the audio stream to a file
    audio_stream = response['AudioStream'].read()
    with open(output, 'wb') as file:
        file.write(audio_stream)


text_to_speech("how are you sir", 'Romanian', "output/audio", output_format='mp3')