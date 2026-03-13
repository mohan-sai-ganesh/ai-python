from openai import OpenAI
import os

client = OpenAI()

audio_file_name = 'sample-audio.mp3'

def save_transcript(text, filename='output/transcript.txt'):
    os.makedirs('output', exist_ok=True)
    with open(filename, 'w') as file:
        file.write(text)
    print(f'Transcript saved to {filename}')

with open(audio_file_name, 'rb') as audio_file:
    response = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file
    )

    save_transcript(response.text)