from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

prompt_message = input('Enter the input: ')

response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = [
        {
            'role': 'user',
            'content': prompt_message
        }
    ]
)

print(response.choices[0].message.content)

# TextOps - Sentiment, Translation, Summarize, Detech Language, Generate Code