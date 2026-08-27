# RetailBrain AI

An AI-powered retail shelf analytics system that applies **Computer Vision and Deep Learning** to detect products on retail shelves, compare object detection models, and support intelligent retail insights.

## Overview

**RetailBrain AI** is a Computer Vision project designed to analyze retail shelf images and detect products using deep learning-based object detection models.

The project explores the complete workflow from **data preparation and augmentation** to **object detection model training and performance evaluation**, with experiments using **YOLOv8** and **Faster R-CNN**.

The goal is to build a reliable foundation for automated retail shelf monitoring and product-level analysis.

---

## Problem Statement

Manual monitoring of retail shelves can be time-consuming and difficult to scale across large numbers of stores and products.

Retail environments require automated systems that can:

* Detect products from shelf images.
* Analyze product presence and shelf occupancy.
* Handle complex retail scenes with multiple products.
* Evaluate different object detection approaches.
* Provide a foundation for automated retail analytics.

RetailBrain AI addresses these challenges using deep learning-based **object detection**.

---

## Solution

The project implements a Computer Vision pipeline that prepares retail image data, trains multiple object detection models, and evaluates their performance.

### Pipeline

```text
Retail Shelf Images
        ↓
Data Preparation
        ↓
Data Augmentation
        ↓
Object Detection Training
        ↓
YOLOv8 ─────────┐
                ├──→ Model Evaluation
Faster R-CNN ───┘
                ↓
Model Comparison
                ↓
Retail Shelf Insights
```

---

## Key Features

* Retail product detection using **YOLOv8**
* Object detection using **Faster R-CNN**
* Image data preparation and augmentation
* Deep learning model training
* Object detection model evaluation
* Performance comparison between models
* Retail shelf analytics foundation
* Interactive application through Streamlit

---

## Dataset

The project uses the **SKU-110K** dataset, a large-scale retail shelf dataset designed for product detection in densely packed shelf images.

The dataset provides challenging retail scenes containing multiple products and visually similar objects, making it suitable for evaluating object detection models in realistic retail environments.

---

## Data Preparation & Augmentation

Before model training, the image data was prepared for object detection experiments.

The workflow included:

* Dataset organization
* Image and annotation preparation
* Data validation
* Preprocessing
* Image augmentation
* Preparation of training-ready data

Data augmentation was used to improve model robustness and help the models generalize to variations in retail shelf images.

---

## Object Detection Models

### YOLOv8

**YOLOv8** was trained for real-time-oriented product detection.

It provides an efficient one-stage object detection approach that is well suited for applications where detection speed and accuracy are both important.

### Faster R-CNN

**Faster R-CNN** was also trained as a second object detection approach.

Unlike YOLOv8, Faster R-CNN follows a two-stage detection architecture, providing a useful baseline for comparing detection performance and model behavior.

---

## Model Evaluation & Comparison

The project includes a dedicated evaluation stage to compare the trained object detection models.

The evaluation workflow focuses on assessing model performance and understanding the trade-offs between different detection approaches.

The comparison helps identify which model is more appropriate for retail shelf analysis based on the observed evaluation results.

---

## My Contributions

As a team member, I contributed to the Computer Vision and Deep Learning pipeline with a focus on:

* Preparing and augmenting the retail image dataset for object detection.
* Training and experimenting with **YOLOv8** for product detection.
* Training and experimenting with **Faster R-CNN**.
* Evaluating object detection model performance.
* Comparing YOLOv8 and Faster R-CNN results to analyze their strengths and limitations.
* Supporting the development of the overall Computer Vision workflow.

---

## Tech Stack

| Category             | Technologies                      |
| -------------------- | --------------------------------- |
| Programming Language | Python                            |
| Computer Vision      | OpenCV                            |
| Deep Learning        | PyTorch                           |
| Object Detection     | YOLOv8, Faster R-CNN              |
| Data Processing      | Pandas, NumPy                     |
| Visualization        | Matplotlib                        |
| Application          | Streamlit                         |
| Dataset              | SKU-110K                          |
| Development          | Jupyter Notebook, VS Code, GitHub |

---

## Project Structure

```text
RetailBrain-AI/
│
├── assets/
│
├── models/
│
├── pages/
│
├── results/
│
├── utils/
│
├── 01_Data_Audit_&_EDA.ipynb
├── 02_Data_Cleaning_&_Validation.ipynb
├── 03_Data_Preparation_&_Augmentation.ipynb
├── 04_Yolo v8n_training.ipynb
├── 05__Faster_R_CNN_Training.ipynb
├── 06_Model_Evaluation_&_Comparison-2.ipynb
│
├── RetailBrain.py
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Key Learning Outcomes

This project provided hands-on experience with:

* Computer Vision workflows
* Object detection
* YOLO-based detection
* Faster R-CNN
* Image preprocessing and augmentation
* Deep learning model training
* Model evaluation and comparison
* Working with large-scale retail image datasets
* Building a Computer Vision pipeline for a real-world business domain

---

## Future Improvements

Potential future improvements include:

* Improving object detection accuracy through additional experimentation.
* Optimizing inference speed for real-time retail applications.
* Expanding shelf-level analytics.
* Adding product counting and stock availability estimation.
* Improving recommendation and retail decision-support capabilities.
* Deploying the system as a scalable production application.

---

## Disclaimer

This project is an educational and experimental AI/ML project. Model predictions and generated retail insights should be validated before being used in real-world business decision-making.

---

## Author

**Menna Hamdy Mahmoud**

AI & Machine Learning Developer

* GitHub: [mennahamdy0](https://github.com/mennahamdy0)
* LinkedIn: [mennahamdy0](https://www.linkedin.com/in/mennahamdy0/)
