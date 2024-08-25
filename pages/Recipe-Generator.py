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

def get_gemini_response(image, prompt):
    # Generate a detailed recipe based on the input prompt and the image
    response = model.generate_content([prompt, image], stream=True)
    return "".join(response)

# Initialize the Streamlit app
st.title("Recipe Generator from Food Image")
st.header("Transform Your Food Photos into Delicious Recipes!")

# Engaging content explaining the feature
st.write("""
Have you ever looked at a delicious dish and wondered how to recreate it?
Our **Recipe Generator** uses advanced AI to analyze your food images and generate a complete recipe tailored to that dish.

### How It Works:
1. **Upload an Image**: Choose a photo of your favorite dish.
2. **Get a Recipe**: Click the button, and our AI will generate a recipe including ingredients and cooking instructions.

### Why Use This Feature?
- **Discover New Recipes**: Turn your food photos into new culinary adventures.
- **Easy to Use**: Just upload an image and let the AI do the rest!
- **Enhance Your Cooking Skills**: Learn how to recreate dishes you love with detailed instructions.
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

# Input fields for generating the recipe
uploaded_file = st.file_uploader("Choose an image of the dish...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    submit = st.button("Generate Recipe")

    # Define the prompt for the AI
    input_prompt = """
    You are an expert chef. Write a detailed recipe for the food provided in the given image.
    """

    # When submit is clicked
    if submit:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(image_data, input_prompt)
        st.subheader("Generated Recipe:")
        st.write(response)
else:
    st.warning("Please upload an image to generate a recipe.")