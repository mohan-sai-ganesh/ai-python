import select
import streamlit as st

user_prompt = st.text_area('Ask something!: ')

if user_prompt:
    st.write(f"Generating response for: {user_prompt}")

    # Call llm

# Conversational interface

if 'history' not in st.session_state:
    st.session_state.history = []

user_prompt = st.chat_input('Ask anything')

if user_prompt:
    st.session_state.history.append({ 'role': 'user', 'content': user_prompt })

for msg in st.session_state.history:
    st.chat_message(msg['role']).write(msg['content'])

# File uploder

file = st.file_uploader('Upload a pdf or image to analyze: ', type=['pdf', 'png', 'jpeg'])

if file:
    st.write(f"Processing file: {file.name}")
    # Send to llm for RAG App

# Selectbox

selected_model = st.selectbox(
    'Choose a model: ',
    [
        "gpt-4",
        "gpt-4o",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
        "gemini-1.0-pro",
        "gemini-1.5-pro",
        "palm-2",
    ]
)

if selected_model:
    st.write(f'Selected model: {selected_model}')

# Temperature 0 - 2

selected_temp = st.slider('Temperature: ', min_value=0.0, max_value=2.0, value=0.5)

st.write(f'Selected temperature: {selected_temp}')

user = {
    "id": 101,
    "name": "Ramesh Kumar",
    "email": "ramesh@example.com",
    "age": 28,
    "is_active": True
}

st.json(user)

# Text Summarization

st.title('Text Summarization')

user_prompt = st.text_area('Enter the text to summarize: ')

if st.button('Generate summary'):
    summary = f"Summary: {user_prompt[:50]}"
    st.write(summary)

generated_response = 'In JavaScript, a Symbol is a primitive data type introduced in ES6 (ECMAScript 2015). It represents a unique and immutable value, often used as unique keys for object properties to avoid name collisions.In JavaScript, a Symbol is a primitive data type introduced in ES6 (ECMAScript 2015). It represents a unique and immutable value, often used as unique keys for object properties to avoid name collisions.In JavaScript, a Symbol is a primitive data type introduced in ES6 (ECMAScript 2015). It represents a unique and immutable value, often used as unique keys for object properties to avoid name collisions.In JavaScript, a Symbol is a primitive data type introduced in ES6 (ECMAScript 2015). It represents a unique and immutable value, often used as unique keys for object properties to avoid name collisions.In JavaScript, a Symbol is a primitive data type introduced in ES6 (ECMAScript 2015). It represents a unique and immutable value, often used as unique keys for object properties to avoid name collisions.'

st.download_button(
    label='Download summary',
    data=generated_response,
    file_name='summary.txt',
    mime='text/plain'
)