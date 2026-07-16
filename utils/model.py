from ultralytics import YOLO
import streamlit as st


@st.cache_resource
def load_model():

    model = YOLO("models/best.pt")

    return model
