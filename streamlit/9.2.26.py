import streamlit as st
from openai import OpenAI
import os

# st.title('Summarize Report')
# client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# prompt = st.text_input('Enter the prompt: ')

# if st.button('Generate'):
#     with st.spinner('Generating response...'):
#         response = client.chat.completions.create(
#             model = 'gpt-4o-mini',
#             messages = [
#                 {
#                     'role': 'system',
#                     'content': 'You are assistant that summarizes the report'
#                 },
#                 {
#                     'role': 'user',
#                     'content': f"Summarize this in 3 bullet points: {prompt}"
#                 }
#             ]
#         )
#         st.toast('Generated summary successfully')

#         st.write(response.choices[0].message.content)

# import streamlit as st
# from openai import OpenAI
# import base64

# # Initialize OpenAI client
# client = OpenAI()

# st.set_page_config(page_title="Image Generator", page_icon="🎨")

# st.title("🎨 AI Image Generator")

# # -------- Sidebar Controls --------
# model_choice = st.sidebar.selectbox(
#     "Choose a model:",
#     [
#         "dall-e-2",
#         "dall-e-3",
#         "gpt-image-1",
#     ]
# )

# num_of_images = st.sidebar.slider("No of images:", 1, 5, 2)

# temperature = st.sidebar.slider("Temperature:", 0.0, 2.0, 0.5)

# st.sidebar.write(
#     f"Selected model: **{model_choice}**  \n"
#     f"Images: **{num_of_images}**  \n"
#     f"Temperature: **{temperature}**"
# )

# # -------- Prompt Input --------
# prompt = st.text_area(
#     "Enter image prompt",
#     placeholder="A futuristic cricket stadium in Mumbai at night, ultra realistic"
# )

# # -------- Generate Button --------
# if st.button("Generate Images 🚀"):
#     if not prompt.strip():
#         st.warning("Please enter a prompt")
#     else:
#         with st.spinner("Generating images... ⏳"):
#             response = client.images.generate(
#                 model=model_choice,
#                 prompt=prompt,
#                 n=num_of_images,
#                 size="1024x1024"
#             )

#         st.success("Images generated successfully ✅")

#         # -------- Display Images --------
#         for i, image_data in enumerate(response.data):

#             # Case 1: Base64 image (gpt-image-1)
#             if image_data.b64_json:
#                 image_bytes = base64.b64decode(image_data.b64_json)
#                 st.image(image_bytes, caption=f"Image {i+1}", use_container_width=True)

#             # Case 2: URL image (dall-e-2 / dall-e-3)
#             elif image_data.url:
#                 st.image(image_data.url, caption=f"Image {i+1}", use_container_width=True)

#             else:
#                 st.error("No image data returned")