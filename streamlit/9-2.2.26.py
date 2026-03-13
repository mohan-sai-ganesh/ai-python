from typing import Any


import streamlit as st
from openai import OpenAI
import os
import base64

tab1, tab2 = st.tabs(['Text Generation', 'Image Generation'])

with tab1:
    st.title('Summarize Report')
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    prompt = st.text_input('Enter the prompt: ')

    if st.button('Generate'):
        with st.spinner('Generating response...'):
            response = client.chat.completions.create(
                model = 'gpt-4o-mini',
                messages = [
                    {
                        'role': 'system',
                        'content': 'You are assistant that summarizes the report'
                    },
                    {
                        'role': 'user',
                        'content': f"Summarize this in 3 bullet points: {prompt}"
                    }
                ]
            )
            st.toast('Generated summary successfully')

            st.write(response.choices[0].message.content)

with tab2:
    prompt = st.text_area(
        "Enter image prompt",
        placeholder="A futuristic cricket stadium in Mumbai at night, ultra realistic"
    )

    if st.button("Generate Image"):
        with st.spinner("Generating images..."):
            response = client.images.generate(
                model='gpt-image-1',
                prompt=prompt,
                n=1,
                size="1024x1024"
            )

        st.success("Images generated successfully")

        # -------- Display Image --------
        if response.data[0].b64_json:
            image_bytes = base64.b64decode(response.data[0].b64_json)
            st.image(image_bytes, caption=f"Image", use_container_width=True)