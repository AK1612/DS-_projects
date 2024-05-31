import streamlit as st
# Set the page title and icon
st.set_page_config(page_title="phonepe Data Visualisation")

# Create a container for the logo and title
col1, col2 = st.columns([1, 2])

# Add the logo to the first column
with col1:
    st.image("photo.png", width=100)

# Add the title to the second column
with col2:
    st.title("PhonePe Data Visualisation")
st.sidebar.success("select page above.")

