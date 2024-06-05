import streamlit as st
from PIL import Image
import pytesseract
import os

# Specify the path to the Vietnamese trained data for Tesseract
pytesseract.pytesseract.tesseract_cmd ='tesseract'
tessdata_dir_config = '--tessdata-dir "."'

st.title("Vietnamese OCR using Tesseract")

uploaded_files = st.file_uploader("Upload one or more images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Recognizing...")

        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(image, lang='vie', config=tessdata_dir_config)
        
        st.write("**Extracted Text:**")
        st.text_area(label='', value=text, height=200)
        st.write("")
        st.download_button(label='Copy to Clipboard', data=text, mime='text/plain', file_name='extracted_text.txt')
