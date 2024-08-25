import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Gemini Suite", page_icon="🌟")

# Custom CSS for a modern look
custom_css = """
<style>
    body {
        background-color: #f9f9f9;  /* Light background for a clean look */
        font-family: 'Arial', sans-serif;  /* Modern font */
    }
    .stButton {
        background-color: #007BFF;  /* Bootstrap primary blue */
        color: white;                /* White text color */
        border: none;                /* No border */
        padding: 12px 24px;         /* Padding */
        text-align: center;          /* Center text */
        text-decoration: none;       /* No underline */
        display: inline-block;       /* Inline-block display */
        margin: 10px 5px;           /* Margin */
        cursor: pointer;             /* Pointer cursor on hover */
        border-radius: 5px;         /* Rounded corners */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .stButton:hover {
        background-color: #0056b3;  /* Darker blue on hover */
    }
    h1 {
        color: #333;                 /* Dark grey text for headers */
        font-size: 2.5em;           /* Larger header */
        margin-bottom: 10px;        /* Space below header */
    }
    h2 {
        color: #555;                 /* Medium grey text for subheaders */
        margin-bottom: 20px;        /* Space below subheader */
    }
    p {
        color: #666;                 /* Light grey text for paragraphs */
        line-height: 1.6;           /* Line height for readability */
        margin-bottom: 20px;        /* Space below paragraphs */
    }
</style>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Landing Page Content
st.title("Welcome to Gemini Suite")
st.subheader("Your AI-Powered Productivity Hub")

st.write("""
Gemini Suite is designed to streamline your workflow and enhance your productivity with cutting-edge AI tools. 
Explore our features below to see how we can help you achieve your goals efficiently.
""")


# Additional Content Section
st.write("---")  # Horizontal line for separation
st.header("Why Choose Gemini Suite?")
st.write("""
- **User-Friendly Interface**: Our intuitive design makes it easy for anyone to use.
- **AI-Driven Insights**: Leverage the power of AI to make informed decisions.
- **Seamless Integration**: Easily connect with your existing tools and workflows.
- **24/7 Support**: Our dedicated support team is here to assist you anytime.
""")

st.write("---")  # Horizontal line for separation
st.header("Get Started Today!")
st.write("""
Join the Gemini Suite community and transform the way you work. Click on the buttons above to explore our features, 
and see how we can help you maximize your productivity.
""")