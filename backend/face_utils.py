import cv2
import numpy as np
import face_recognition
import hashlib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("face_utils")

# Lower = more strict. 0.45 is fairly strict for security.
SIMILARITY_THRESHOLD = 0.45


# ---------------------------------------
# Validate image before using it
# ---------------------------------------
def _validate_image(img):
    if img is None:
        raise ValueError("Image is None")

    if not isinstance(img, np.ndarray):
        raise ValueError("Image is not a numpy array")

    if img.size == 0:
        raise ValueError("Image array is empty")

    if len(img.shape) != 3 or img.shape[2] != 3:
        raise ValueError(f"Invalid image shape: {img.shape}")

    return True