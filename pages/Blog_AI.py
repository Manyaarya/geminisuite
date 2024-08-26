from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def get_blog_response(image, title, description, keywords):
    prompt = f"Generate a blog post based on the image of the dish. Title: {title}. Description: {description}. Keywords: {keywords}."
    # Generate content based on the prompt and image
    response = model.generate_content([image[0], prompt])
    return response.text

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

# Initialize our Streamlit app
st.title("Blog Generator from Image")

# Inputs for blog generation
title = st.text_input("Blog Title:", placeholder="Enter a catchy title for your blog")
description = st.text_area("Blog Description:", placeholder="Describe the blog content briefly")
keywords = st.text_input("Keywords (comma-separated):", placeholder="e.g., recipe, cooking, food")

uploaded_file = st.file_uploader("Choose an image of the dish...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Generate Blog Post")

if submit:
    image_data = input_image_details(uploaded_file)
    blog_post = get_blog_response(image_data, title, description, keywords)
    st.subheader("Generated Blog Post:")
    st.write(blog_post)

    # Feature to save the generated recipe
    st.download_button(
        label="Save Recipe",
        data=blog_post,
        file_name=f"{title.replace(' ', '_')}_recipe.txt",
        mime="text/plain"
    )