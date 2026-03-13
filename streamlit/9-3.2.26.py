import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header('GPT-4 Output: ')
    st.write('AI says: Hello from GPT-4')

with col2:
    st.header('Llama 3 Output: ')
    st.write('AI says: Hello from Llama 3')

with col3:
    st.header('Claude 2.5 Output: ')
    st.write('AI says: Hello from Claude 2.5')
