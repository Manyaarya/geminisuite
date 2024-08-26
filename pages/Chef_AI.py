from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import json
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

def save_recipe(title, recipe):
    # Save the recipe to a JSON file
    if not os.path.exists('recipes.json'):
        print("Creating new recipes.json file.")  # Debugging output
        with open('recipes.json', 'w') as f:
            json.dump([], f)  # Create an empty list if the file does not exist

    try:
        with open('recipes.json', 'r+') as f:
            recipes = json.load(f)
            recipes.append({"title": title, "recipe": recipe})
            f.seek(0)
            json.dump(recipes, f)
            print(f"Saved recipe: {title}")  # Debugging output
    except Exception as e:
        print(f"Error saving recipe: {e}")  # Catch and print any errors

def load_recipes():
    # Load saved recipes from the JSON file
    if os.path.exists('recipes.json'):
        with open('recipes.json', 'r') as f:
            recipes = json.load(f)
            print(f"Loaded recipes: {recipes}")  # Debugging output
            return recipes
    print("No recipes file found.")  # Debugging output
    return []

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

    # Input for recipe title
    recipe_title = st.text_input("Recipe Title:", placeholder="Enter a title for your recipe")

    # Button to save the recipe
    if st.button("Save Recipe"):
        if recipe_title:
            save_recipe(recipe_title, recipe)
            st.success(f"Recipe '{recipe_title}' saved successfully!")
        else:
            st.error("Please enter a title for the recipe.")

# Load and display saved recipes
st.subheader("Saved Recipes:")
saved_recipes = load_recipes()
if saved_recipes:
    for saved in saved_recipes:
        st.write(f"**{saved['title']}**")
        st.write(saved['recipe'])
else:
    st.write("No recipes saved yet.")