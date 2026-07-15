import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile
import os

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="RetailBrain AI",
    page_icon="🛒",
    layout="wide"
)

# ============================================================
# Load Model
# ============================================================

@st.cache_resource
def load_model():
    model = YOLO("models/best.pt")
    return model

model = load_model()

# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("RetailBrain AI")

st.sidebar.markdown("---")

confidence = st.sidebar.slider(
    "Confidence Threshold",
    0.10,
    1.00,
    0.25,
    0.05
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Smart Retail Shelf Monitoring

Models Used:

• YOLOv8

• Faster R-CNN

Dataset:

SKU110K
"""
)

# ============================================================
# Main Title
# ============================================================

st.title("🛒 Smart Retail Shelf Monitoring")

st.write(
"""
Upload a retail shelf image to detect products,
count items, and analyze shelf status.
"""
)

# ============================================================
# Upload Image
# ============================================================

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg","jpeg","png"]
)

# ============================================================
# Detection
# ============================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    image = image.convert("RGB")

    col1,col2 = st.columns(2)

    with col1:

        st.subheader("Original Image")

        st.image(image,use_container_width=True)

    temp = tempfile.NamedTemporaryFile(
        suffix=".jpg",
        delete=False
    )

    image.save(temp.name)

    results = model.predict(

        source=temp.name,

        conf=confidence,

        save=False,

        verbose=False

    )

    result = results[0].plot()

    result = cv2.cvtColor(
        result,
        cv2.COLOR_BGR2RGB
    )

    with col2:

        st.subheader("Detection Result")

        st.image(
            result,
            use_container_width=True
        )

    # ========================================================
    # Analytics
    # ========================================================

    total_products = len(results[0].boxes)

    st.markdown("---")

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Detected Products",
        total_products
    )

    occupancy = min(
        100,
        round(total_products/200*100)
    )

    c2.metric(
        "Shelf Occupancy",
        f"{occupancy}%"
    )

    if occupancy < 40:

        status = "Low Stock"

    elif occupancy < 70:

        status = "Medium"

    else:

        status = "Well Stocked"

    c3.metric(
        "Shelf Status",
        status
    )

    # ========================================================
    # Recommendation
    # ========================================================

    st.markdown("---")

    st.subheader("Recommendation")

    if occupancy < 40:

        st.error(
            "Shelf needs immediate restocking."
        )

    elif occupancy < 70:

        st.warning(
            "Shelf stock is moderate. Consider restocking soon."
        )

    else:

        st.success(
            "Shelf stock level is good."
        )

    # ========================================================
    # Download Image
    # ========================================================

    output = cv2.cvtColor(
        result,
        cv2.COLOR_RGB2BGR
    )

    _,buffer = cv2.imencode(
        ".jpg",
        output
    )

    st.download_button(

        label="Download Result",

        data=buffer.tobytes(),

        file_name="prediction.jpg",
  mime="image/jpeg"

    )

# ============================================================
# Footer
# ============================================================

st.markdown("---")

st.caption(
"RetailBrain AI | Smart Retail Shelf Monitoring using YOLOv8 and Faster R-CNN"
)
