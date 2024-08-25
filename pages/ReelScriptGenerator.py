from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the Generative AI model with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the Gemini model for generating responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Function to generate a reel script
def generate_reel_script(topic, tone, target_audience, specific_requirements):
    prompt = f"Create a reel script for a topic called {topic}. The tone should be {tone}, targeting {target_audience}. Specific requirements include {specific_requirements}."
    response = get_gemini_response(prompt)
    return response

# Initialize the Streamlit app
st.title("Reel Script Generator")
st.header("Generate Engaging Scripts for Your Reels!")

# Input fields for generating the script
input_topic = st.text_input("Topic:")
input_tone = st.selectbox("Tone", ["Funny", "Serious", "Informative"])
input_target_audience = st.text_input("Target Audience:")
input_specific_requirements = st.text_input("Specific Requirements:")
submit = st.button("Generate Script")

# When submit is clicked
if submit:
    script = generate_reel_script(input_topic, input_tone, input_target_audience, input_specific_requirements)
    st.subheader("The generated script is:")
    st.write(script)

# Engaging content explaining the feature
st.write("""
Creating engaging and captivating scripts for your Instagram Reels can be a challenge. 
Our **Reel Script Generator** leverages the power of AI to help you craft the perfect script tailored to your needs.

### What Can You Do with This Feature?
- **Generate Unique Scripts**: Input your topic and let the AI create a unique script that resonates with your audience.
- **Customize Tone and Style**: Choose from various tones such as Funny, Serious, or Informative to match your brand's voice.
- **Target Audience Focus**: Specify your target audience to ensure the script speaks directly to them, enhancing engagement.
- **Specific Requirements**: Include any specific details or requirements, and the AI will incorporate them into the script.

### How It Works
1. **Enter Your Topic**: Describe the main idea or theme of your reel.
2. **Select a Tone**: Choose the tone that best fits your content style.
3. **Define Your Audience**: Specify who you are targeting with your reel.
4. **Add Specific Requirements**: Include any additional details you want the script to cover.
5. **Generate Your Script**: Click the button, and watch as the AI crafts a compelling script for you!

With our Reel Script Generator, you can save time and unleash your creativity, making content creation a breeze. 
Whether you're a content creator, marketer, or business owner, this tool is designed to help you produce engaging reels that stand out.
""")

