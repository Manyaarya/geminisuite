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

def get_gemini_response(image, tone, topic, target_audience):
    # Generate a blog post based on the input prompt, image, tone, topic, and target audience
    prompt = f"Write a blog post with a {tone} tone about {topic} for a target audience of {target_audience}. Use the provided image as inspiration."
    response = model.generate_content([prompt, image], stream=True)
    return "".join(response)

# Initialize the Streamlit app
st.title("Blog Generator from Image")
st.header("Turn Your Photos into Engaging Blog Posts!")

# Engaging content explaining the feature
st.write("""
Struggling to come up with blog post ideas? Let our AI-powered Blog Generator help!
Simply upload an image, provide some details, and our advanced algorithms will generate a complete blog post tailored to your needs.

### How It Works:
1. **Upload an Image**: Choose a photo related to your blog topic.
2. **Provide Details**: Enter a tone, topic, and target audience for your blog post.
3. **Generate Blog**: Click the button, and our AI will generate an engaging blog post inspired by your image and inputs.

### Why Use This Feature?
- **Boost Your Creativity**: Turn your photos into unique blog post ideas.
- **Save Time**: Let the AI handle the writing while you focus on other aspects of your blog.
- **Tailor to Your Audience**: Generate content that resonates with your target readers.
""")

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

# Input fields for generating the blog post
uploaded_file = st.file_uploader("Choose an image related to your blog topic...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    tone = st.selectbox("Select a tone for your blog post:", ["Informative", "Persuasive", "Humorous", "Inspirational"])
    topic = st.text_input("Enter a topic for your blog post:")
    target_audience = st.text_input("Who is your target audience?")

    submit = st.button("Generate Blog Post")

    # When submit is clicked
    if submit:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(image_data, tone, topic, target_audience)
        st.subheader("Generated Blog Post:")
        st.write(response)
else:
    st.warning("Please upload an image and provide details to generate a blog post.")