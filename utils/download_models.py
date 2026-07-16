import os
import gdown

# ================================
# Faster R-CNN
# ================================

FRCNN_PATH = "models/best_fasterrcnn.pth"

FRCNN_URL = "https://drive.google.com/uc?id=1c1HCmJIhpsF_jfosMAUjw9FTTwuoteeE"


def download_fasterrcnn():

    if not os.path.exists(FRCNN_PATH):

        os.makedirs("models", exist_ok=True)

        gdown.download(
            FRCNN_URL,
            FRCNN_PATH,
            quiet=False
        )
