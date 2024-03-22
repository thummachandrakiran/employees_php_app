import streamlit as st

from PIL import Image

image_file = Image.open("Image.jpg")

st.image(image_file)
