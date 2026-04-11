# Serves as a placeholder for where the classifier logic will live

from ultralytics import YOLO

model = YOLO("best.pt")

RECYCLING_CLASSES = ["cardboard", "glass", "metal", "paper", "plastic"]
TRASH_CLASSES = ["Trash"]

def get_bin_category(frame):
    results = model(frame, verbose=False)

    if len(results[0].boxes) == 0:
        return None 

    best_detection = results[0].boxes[0]
    class_id = int(best_detection.cls[0].item())
    class_name = model.names[class_id]
    confidence = float(best_detection.conf[0].item())

    if confidence < 0.70:
        return None 

    # --- THE FIX: Completely ignore the cardboard class ---
    if class_name == "cardboard":
        return None

    print(f"AI Detected: {class_name} ({confidence:.1%} confident)")

    if class_name in RECYCLING_CLASSES:
        return "recycling"
    else:
        return "trash"