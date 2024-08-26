from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def get_recipe_response(image):
    prompt = "Generate a recipe based on the image of the dish."
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
st.title("Recipe Generator from Image")

uploaded_file = st.file_uploader("Choose an image of the dish...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Generate Recipe")

if submit:
    image_data = input_image_details(uploaded_file)
    recipe = get_recipe_response(image_data)
    st.subheader("Recipe:")
    st.write(recipe)