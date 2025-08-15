
from ultralytics import YOLO
import cv2
import numpy as np
import os

# Load the model once globally
model = YOLO("best.pt")
class_names = model.names

def detect_potholes(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image could not be read. Check file format or path.")

    img = cv2.resize(img, (1020, 500))
    h, w, _ = img.shape

    results = model.predict(img)
    detected = False
    pothole_count = 0

    for r in results:
        boxes = r.boxes
        masks = r.masks

    if masks is not None and len(masks) > 0:
        masks = masks.data.cpu()
        pothole_count = len(masks)
        detected = True

        for seg, box in zip(masks.numpy(), boxes):
            seg = cv2.resize(seg, (w, h))
            contours, _ = cv2.findContours((seg).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                d = int(box.cls)
                c = class_names[d]
                x, y, x1, y1 = cv2.boundingRect(contour)
                cv2.polylines(img, [contour], True, color=(0, 0, 255), thickness=2)
                cv2.putText(img, c, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    else:
        cv2.putText(img, "No potholes detected", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Save the processed image
    filename = os.path.basename(image_path)
    processed_path = os.path.join("static","detected_potholes", filename)
    cv2.imwrite(processed_path, img)

    return processed_path, pothole_count
