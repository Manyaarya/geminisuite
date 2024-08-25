import streamlit as st

# Set up the page configuration - must be the first Streamlit command
st.set_page_config(page_title="My Multipage App", page_icon="🌟")

# Landing Page Content
st.title("Welcome to My Multipage App")
st.subheader("Explore our exciting features!")

# Display the logo
st.image("logo.jpg", use_column_width=True)

# Navigation Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Caption Generator"):
        import pages.caption_generator
        pages.caption_generator.app()

with col2:
    if st.button("Other Feature"):
        import pages.other_feature
        pages.other_feature.app()

with col3:
    if st.button("Vision"):
        import pages.vision
        pages.vision.app()