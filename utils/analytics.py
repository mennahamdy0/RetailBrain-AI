"""
Analytics Utilities
"""

import numpy as np
import pandas as pd


# ==========================================
# Detection Statistics
# ==========================================

def get_statistics(result):

    total_products = len(result.boxes)

    if total_products > 0:

        confidences = result.boxes.conf.cpu().numpy()

        average_confidence = float(np.mean(confidences))
        max_confidence = float(np.max(confidences))
        min_confidence = float(np.min(confidences))

    else:

        average_confidence = 0.0
        max_confidence = 0.0
        min_confidence = 0.0

    return {

        "products": total_products,

        "avg_confidence": average_confidence,

        "max_confidence": max_confidence,

        "min_confidence": min_confidence

    }


# ==========================================
# Detection Table
# ==========================================

def detection_table(result):

    rows = []

    boxes = result.boxes

    if len(boxes) == 0:

        return pd.DataFrame(
            columns=[
                "ID",
                "Class",
                "Confidence"
            ]
        )

    classes = boxes.cls.cpu().numpy()
    confidences = boxes.conf.cpu().numpy()

    for i in range(len(boxes)):

        rows.append({

            "ID": i + 1,

            "Class": int(classes[i]),

            "Confidence": round(float(confidences[i]), 3)

        })

    return pd.DataFrame(rows)


# ==========================================
# Class Distribution
# ==========================================

def class_distribution(result):

    boxes = result.boxes

    if len(boxes) == 0:

        return pd.DataFrame(
            columns=[
                "Class",
                "Count"
            ]
        )

    classes = boxes.cls.cpu().numpy().astype(int)

    unique, counts = np.unique(
        classes,
        return_counts=True
    )

    return pd.DataFrame({

        "Class": unique,

        "Count": counts

    })


# ==========================================
# Recommendation Features
# ==========================================

def recommendation_features(result):

    statistics = get_statistics(result)

    return {

        "total_products": statistics["products"],

        "average_confidence": statistics["avg_confidence"],

        "max_confidence": statistics["max_confidence"],

        "min_confidence": statistics["min_confidence"]

    }
