import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="My Web App", page_icon="🌐", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
st.sidebar.button("Home")
st.sidebar.button("About")
st.sidebar.button("Contact")

# Main Content
st.title("Welcome to My Website! 🚀")
st.subheader("A modern, interactive web app using Streamlit")

# Create columns
col1, col2 = st.columns([2, 1])

with col1:
    st.image("https://source.unsplash.com/800x400/?technology", use_column_width=True)
    st.markdown(
        """### Features:
        - 📌 Simple and easy UI
        - 🚀 Fast and interactive experience
        - 📊 Data visualization support
        - 🔗 Responsive design
        """
    )
    
with col2:
    st.markdown("### User Input")
    user_name = st.text_input("Enter your name:")
    user_feedback = st.text_area("Share your thoughts:")
    if st.button("Submit"):
        st.success(f"Thank you, {user_name}! Your feedback is recorded.")

# Footer
st.markdown("---")
st.markdown("© 2025 My Web App. All rights reserved.")
