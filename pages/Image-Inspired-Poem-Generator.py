from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the Generative AI model with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the Gemini model for generating responses
model = genai.GenerativeModel("gemini-1.5-flash-latest")



def get_poem_from_image(image, tone, style):
    # Generate a poem based on the input image, tone, and style
    prompt = f"Create a {tone} {style} poem inspired by the following image."
    response = model.generate_content([prompt, image], stream=True)
    return "".join(response)

# In the Streamlit app
st.header("Image-Inspired Poem Generator")

uploaded_file = st.file_uploader("Upload an image for your poem...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    tone = st.selectbox("Select a tone for your poem:", ["Joyful", "Melancholic", "Reflective", "Energetic"])
    style = st.selectbox("Select a style for your poem:", ["Haiku", "Sonnet", "Free Verse", "Acrostic"])

    submit = st.button("Generate Poem")

    if submit:
        image_data = input_image_details(uploaded_file)
        poem_response = get_poem_from_image(image_data, tone, style)
        st.subheader("Generated Poem:")
        st.write(poem_response)
else:
    st.warning("Please upload an image to generate a poem.")