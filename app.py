from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini models to get responses
model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# function to generate a reel script
def generate_reel_script(topic, tone, target_audience, specific_requirements):
    prompt = f"Create a reel script for a topic called {topic}. The tone should be {tone}, targeting {target_audience}. Specific requirements include {specific_requirements}."
    response = get_gemini_response(prompt)
    return response


## initialize our streamlit app
st.set_page_config(page_title="Reel Script Generator")

st.header("Reel Script Generator")

input_topic = st.text_input("Topic:")
input_tone = st.selectbox("Tone", ["Funny", "Serious", "Informative"])
input_target_audience = st.text_input("Target Audience:")
input_specific_requirements = st.text_input("Specific Requirements:")
submit = st.button("Generate Script")

## When submit is clicked
if submit:
    script = generate_reel_script(input_topic, input_tone, input_target_audience, input_specific_requirements)
    st.subheader("The generated script is:")
    st.write(script)