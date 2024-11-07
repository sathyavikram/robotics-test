from gpiozero import Motor
from time import sleep

# Initialize the Motor using GPIO pins 17 and 27
motor = Motor(forward=17, backward=27)

try:
    while True:
        # Run motor forward at full speed
        motor.forward()
        print("Motor running forward")
        sleep(5)

        # Run motor backward at full speed
        motor.backward()
        print("Motor running backward")
        sleep(5)

        # Stop the motor
        motor.stop()
        sleep(5)
        print("Motor stopped")

except KeyboardInterrupt:
    # Cleanup
    motor.stop()
    print("Motor control interrupted and stopped")

finally:
    motor.close()