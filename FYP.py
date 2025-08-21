import os
import streamlit as st
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from gtts import gTTS

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Create "audio" directory if it doesn't exist
AUDIO_DIR = "audio"
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

# Function to generate a single caption
def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    caption_ids = model.generate(**inputs, max_length=30, num_return_sequences=1)
    caption = processor.batch_decode(caption_ids, skip_special_tokens=True)[0]
    return caption

# Function to generate and save audio for the caption
def text_to_speech(text, filename="caption_audio.mp3"):
    audio_path = os.path.join(AUDIO_DIR, filename)
    tts = gTTS(text=text, lang="en")
    tts.save(audio_path)
    return audio_path

# Streamlit UI
st.title("🖼️ AI Image Captioning App 🚀")
st.write("Upload an image and get an AI-generated caption with audio!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = generate_caption(uploaded_file)
        
        st.success("✅ Caption Generated!")
        st.write(f"**Caption:** {caption}")


         # Option to download caption
        caption_file = "caption.txt"
        with open(caption_file, "w") as file:
            file.write(caption)
        st.download_button("Download Caption", caption, file_name="caption.txt", mime="text/plain")
        
        # Convert caption to speech
        audio_file = text_to_speech(caption, "caption_audio.mp3")
        st.audio(audio_file, format="audio/mp3")
