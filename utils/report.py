"""
Report Utilities
"""

import pandas as pd


def create_report(statistics):

    report = pd.DataFrame({

        "Metric":[

            "Total Products",

            "Average Confidence"

        ],

        "Value":[

            statistics["products"],

            round(statistics["avg_confidence"],3)

        ]

    })

    return report
