
import pandas as pd


def load_results():

    data = {

        "Model": [

            "YOLOv8 Nano",

            "YOLOv8 Small",

            "Faster R-CNN"

        ],

        "mAP50": [

            0.78,

            0.84,

            0.81

        ],

        "Precision": [

            0.88,

            0.91,

            0.89

        ],

        "Recall": [

            0.82,

            0.87,

            0.85

        ],

        "Inference Time": [

            0.021,

            0.037,

            0.120

        ]

    }

    return pd.DataFrame(data)
