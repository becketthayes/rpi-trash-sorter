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

    # TWEAK 1: Give the sensor 2 seconds to adjust to the lighting
    time.sleep(2)

    print("Camera started (Headless Mode). Press Ctrl+C to quit.")

    try:
        while True:
            # TWEAK 2: Explicitly grab from the "main" configuration
            frame = picam2.capture_array("main")

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
            
            # TWEAK 3: Rest for half a second before taking the next picture.
            # This prevents the AI from frying the CPU when the bin is empty.
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nExiting program")

    finally:
        picam2.stop()
        print("Camera safely closed.")

if __name__ == "__main__":
    main()