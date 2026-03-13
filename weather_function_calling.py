from openai import OpenAI
import os
import requests
import json

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_current_weather_info(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=96e1c5b39aaf64661a550fd1fc6f0486&units=metric'
    response = requests.get(url)
    data = response.json()
    return {
        'city': city,
        'temperature': data['main']['temp'],
        'condition': data['weather'][0]['description']
    }

# print(get_current_weather_info('Hyderabad'))

# What is current weather of Hyderabad

def ask_weather(user_question):
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            {
                'role': 'system',
                'content': 'You are a sentiment analysis assistant'
            },
            {
                'role': 'user',
                'content': user_question
            }
        ],
        tools=[
            {
                'type': 'function',
                'function': {
                    'name': 'get_current_weather_info',
                    'description': 'Get current weather information for a given city',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'city': { 'type': 'string' },
                        },
                        'required': ['city']
                    }
                }
            },
        ],
        tool_choice='auto'
    )

    choice = response.choices[0]
    message = choice.message
    
    if not message.tool_calls:
        return response.choices[0].message.content
    else:
        tool_call = response.choices[0].message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)    
        city = args['city']
        tool_response = get_current_weather_info(city)
        
        response = client.chat.completions.create(
        model = 'gpt-4o-mini',
            messages = [
                {
                    'role': 'system',
                    'content': 'You are a rephrase sentence assistant'
                },
                {
                    'role': 'user',
                    'content': f"Give response in a normal user understandable language: {tool_response}"
                }
            ],
        )
        return response.choices[0].message.content


result = ask_weather("What's the current temperature of Hyderabad?")
print(result)