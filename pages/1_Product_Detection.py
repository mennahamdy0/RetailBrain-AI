import streamlit as st
from PIL import Image
import tempfile

from utils.model import load_model

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Product Detection",
    page_icon="📦",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📦 Product Detection")

st.markdown("""
Upload a retail shelf image to detect products using the trained YOLOv8 model.
""")

st.divider()

# --------------------------------------------------
# Upload Image
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Shelf Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# Display Image
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original Image")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.subheader("Detection Results")

        st.info("Click 'Run Detection' to start the model.")

# --------------------------------------------------
# Detection Button
# --------------------------------------------------

st.divider()

if st.button("🚀 Run Detection", use_container_width=True):

    st.success("YOLO model will be integrated in the next step.")
