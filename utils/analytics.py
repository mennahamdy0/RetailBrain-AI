"""
Analytics Utilities
"""

import numpy as np
import pandas as pd


def get_statistics(result):

    total_products = len(result.boxes)

    if total_products > 0:

        confidences = result.boxes.conf.cpu().numpy()

        average_confidence = float(np.mean(confidences))

    else:

        average_confidence = 0.0

    return {

        "products": total_products,

        "avg_confidence": average_confidence

    }


def detection_table(result):

    rows = []

    boxes = result.boxes

    if len(boxes) == 0:

        return pd.DataFrame(columns=[
            "ID",
            "Confidence"
        ])

    for i, conf in enumerate(boxes.conf.cpu().numpy(), start=1):

        rows.append({

            "ID": i,

            "Confidence": round(float(conf),3)

        })

    return pd.DataFrame(rows)
