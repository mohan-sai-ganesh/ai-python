import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI()

# Create output folder
os.makedirs("output", exist_ok=True)

def save_transcript(text, filename="output/transcript.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

st.set_page_config(page_title="Audio Transcription", page_icon="🎧")

st.title("🎧 Audio to Text Transcription")
st.write("Upload an audio file (mp3, wav, m4a) to get transcription.")

# File uploader
uploaded_file = st.file_uploader(
    "Upload audio file",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file is not None:
    st.audio(uploaded_file)

    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing... Please wait ⏳"):
            # Save uploaded audio temporarily
            audio_path = f"output/{uploaded_file.name}"
            with open(audio_path, "wb") as f:
                f.write(uploaded_file.read())

            # OpenAI transcription
            with open(audio_path, "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )

            transcript_text = response.text

            # Save transcript
            save_transcript(transcript_text)

        st.success("Transcription completed ✅")

        # Display transcript
        st.subheader("📝 Transcript")
        st.text_area("Transcribed Text", transcript_text, height=300)

        # Download option
        st.download_button(
            label="⬇️ Download Transcript",
            data=transcript_text,
            file_name="transcript.txt",
            mime="text/plain"
        )
