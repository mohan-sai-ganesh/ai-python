from openai import OpenAI
import os
import time

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def fine_tune_it_routing():
    
    # Upload the training data
    # upload_response = client.files.create(
    #     file = open('it_ticket_training.jsonl', 'rb'),
    #     purpose = 'fine-tune'
    # )

    # print(upload_response)

    # Create a fine-tune job
    # job_response = client.fine_tuning.jobs.create(
    #     model = 'gpt-3.5-turbo',
    #     training_file='file-GeXVVz2ha5SzvMVpBFTXTr'
    # )

    # while(True):
    #     job_response = client.fine_tuning.jobs.retrieve(job_response.id)
    #     print('Job status: ', job_response.status)

    #     if job_response.status in ['succeeded', 'failed']:
    #         break

    #     time.sleep(30)
    
    # if job_response.status == 'succeeded':
    #     fine_tuned_model = job_response.fine_tuned_model
    #     print('Fine-tuned model: ', fine_tuned_model)
    # else:
    #     print('Fine-tuning failed')
    #     print('Error: ', job_response.error)


    response = client.chat.completions.create(
        model = 'ft:gpt-3.5-turbo-1106:edify::CkuR3aNh',
        messages = [
            {
                'role': 'user',
                'content': "What is the capital of Telangana"
            }
        ]
    )

    print(response.choices[0].message.content)

fine_tune_it_routing()