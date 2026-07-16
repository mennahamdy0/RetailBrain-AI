import os
import gdown

MODEL_PATH = "models/best_fasterrcnn.pth"

URL = "DIRECT_DOWNLOAD_LINK"

if not os.path.exists(MODEL_PATH):

    gdown.download(
        URL,
        MODEL_PATH,
        quiet=False
    )
