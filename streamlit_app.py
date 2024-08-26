import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="My Multipage App", page_icon="🌟")

# Sidebar with logo
st.header("Gemini Suite")
st.title("Welcome to Gemini Suite")
st.subheader("Your AI-Powered Productivity Hub")

st.write("""
Gemini Suite is designed to streamline your workflow and enhance your productivity with cutting-edge AI tools. 
Explore our features below to see how we can help you achieve your goals efficiently.
""")

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
Join the Gemini Suite community and transform the way you work. Click on the buttons below to explore our features,
and see how we can help you maximize your productivity.
""")

# Create a grid layout for navigation
st.write("---")  # Horizontal line for separation
st.header("Explore Our Features")

# Create columns for the grid
col1, col2, col3, col4 = st.columns(4)

# Define the features/pages
features = [
    ("Recipe Generator", "Generate delicious recipes from images.", "recipe_generator"),
    ("Task Manager", "Manage your tasks efficiently.", "task_manager"),
    ("Analytics Dashboard", "Get insights from your data.", "analytics_dashboard"),
    ("Settings", "Customize your experience.", "settings"),
]

# Create buttons in the grid
for i, (title, description, page) in enumerate(features):
    with eval(f"col{i % 4 + 1}"):  # Distribute features across columns
        if st.button(title):
            st.session_state.page = page  # Set the selected page in session state
            st.rerun()  # Rerun the app to navigate to the selected page
        st.write(description)

# Display the selected page content based on session state
if 'page' in st.session_state:
    if st.session_state.page == "Chef_AI":
        st.subheader("Recipe Generator Page")
        st.write("Here you can generate recipes!")
    elif st.session_state.page == "task_manager":
        st.subheader("Task Manager Page")
        st.write("Manage your tasks here!")
    elif st.session_state.page == "analytics_dashboard":
        st.subheader("Analytics Dashboard Page")
        st.write("View your analytics here!")
    elif st.session_state.page == "settings":
        st.subheader("Settings Page")
        st.write("Customize your settings here!")
else:
    st.write("Select a feature to get started.")