# Will be the main file for this project

import cv2 
import time 
from model.classifier import get_bin_category
from picamera2 import Picamera2
from servos.servos import open_recycling, open_trash, close_recycling, close_trash

def main():
    picam2 = Picamera2()

    config = picam2.create_video_configuration(main={"size": (640, 480)})
    picam2.configure(config)
    picam2.start()

    print("Camera started (Headless Mode). Press Ctrl+C to quit.")

    try:
        while True:
            frame = picam2.capture_array()

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            category = get_bin_category(frame)

            if category == "recycling":
                print("Opening RECYCLING bin")
                open_recycling()

                time.sleep(3)
                close_recycling()
                time.sleep(1)

            elif category == "trash":
                print("Opening TRASH bin")
                open_trash()

                time.sleep(3)
                close_trash()
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting program")

    finally:
        picam2.stop()

if __name__ == "__main__":
    main()          