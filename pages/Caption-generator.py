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

def get_gemini_response(image, tone, length, num_captions):
    # Generate captions based on the input image, tone, and length
    prompt = f"Generate {num_captions} {length} captions in a {tone} tone for the following image."
    response = model.generate_content([prompt, image], stream=True)
    return "".join(response)

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize the Streamlit app
st.title("Image Caption Generator")
st.header("Generate Captions for Your Images!")

# Engaging content explaining the feature
st.write("""
In today's visual-centric world, captions play a crucial role in enhancing your images. 
Our **Image Caption Generator** uses advanced AI to analyze your images and generate engaging captions tailored to your needs.

### How It Works:
1. **Upload an Image**: Choose a photo that you want to caption.
2. **Select a Tone**: Choose the tone for your caption (e.g., fun, serious, informative).
3. **Choose Caption Length**: Select the desired length for your captions.
4. **Get Captions**: Click the button, and our AI will generate captions for your image.

### Why Use This Feature?
- **Boost Engagement**: Captions can make your images more relatable and shareable.
- **Save Time**: Quickly generate captions without the hassle of brainstorming.
- **Enhance Storytelling**: Use captions to tell a story or convey a message with your visuals.
""")

# Input fields for generating the caption
uploaded_files = st.file_uploader("Choose images to generate captions...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    captions = []
    for index, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        tone = st.selectbox("Select a tone for your caption:", ["Fun", "Serious", "Informative", "Inspirational"], key=f"tone_{index}")
        length = st.selectbox("Select caption length:", ["Short", "Medium", "Long"], key=f"length_{index}")
        num_captions = st.number_input("Number of captions to generate:", min_value=1, max_value=5, value=1, key=f"num_captions_{index}")

        submit = st.button("Generate Caption", key=f"generate_{index}")

        # When submit is clicked
        if submit:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(image_data, tone, length, num_captions)
            captions.append(response)
            st.subheader("Generated Caption:")
            st.write(response)

    # Provide an option to save captions
    if st.button("Save Captions"):
        with open("captions.txt", "w") as f:
            for caption in captions:
                f.write(caption + "\n")
        st.success("Captions saved to captions.txt!")

    # Simulated social media sharing
    if st.button("Share on Social Media"):
        st.success("Sharing your captions on social media... (simulated)")

    # Simulated translation option
    if st.button("Translate Captions"):
        translated_captions = [f"Translated: {caption}" for caption in captions]
        st.subheader("Translated Captions:")
        for translated_caption in translated_captions:
            st.write(translated_caption)

else:
    st.warning("Please upload at least one image to generate captions.")