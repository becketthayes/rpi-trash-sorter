from gpiozero import Servo

# Assign the servos to their respective GPIO pins
recycling_servo = Servo(18, min_pulse_width=0.0005, max_pulse_width=0.0025)
trash_servo = Servo(12, min_pulse_width=0.0005, max_pulse_width=0.0025)

def open_recycling():
    recycling_servo.max()

def open_trash():
    trash_servo.max()

def close_recycling():
    recycling_servo.min()

def close_trash():
    trash_servo.min()