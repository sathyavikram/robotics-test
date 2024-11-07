from gpiozero import OutputDevice
from time import sleep

# Define GPIO pins for the ULN2003 inputs
IN1 = OutputDevice(17)  # Adjust according to your wiring
IN2 = OutputDevice(18)
IN3 = OutputDevice(27)
IN4 = OutputDevice(22)

# Define step sequence for 28BYJ-48 motor
step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# Function to set GPIO pins based on the step sequence
def set_step(w1, w2, w3, w4):
    IN1.value = w1
    IN2.value = w2
    IN3.value = w3
    IN4.value = w4

# Function to turn motor in one direction
def step_forward(delay, steps):
    for _ in range(steps):
        for step in step_sequence:
            set_step(*step)
            sleep(delay)

# Function to turn motor in the opposite direction
def step_backward(delay, steps):
    for _ in range(steps):
        for step in reversed(step_sequence):
            set_step(*step)
            sleep(delay)

# Main program
try:
    while True:
        steps = 512  # Full rotation for 28BYJ-48
        delay = 0.002  # Adjust for speed
        
        print("Rotating forward...")
        step_forward(delay, steps)

        sleep(1)

        print("Rotating backward...")
        step_backward(delay, steps)

        sleep(1)

except KeyboardInterrupt:
    print("Motor control interrupted.")

finally:
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()
