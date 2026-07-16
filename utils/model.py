"""
Model Loading Utilities
"""

import streamlit as st
from ultralytics import YOLO


@st.cache_resource
def load_model():

    """
    Load the trained YOLO model only once.
    """

    return YOLO("models/best.pt")
