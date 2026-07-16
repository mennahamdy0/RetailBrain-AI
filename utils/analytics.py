
"""
Analytics Utilities
"""

import numpy as np


def get_statistics(result):

    """
    Calculate detection statistics.
    """

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
