import RPi.GPIO as GPIO
import time

# use example from https://www.electronicshub.org/raspberry-pi-stepper-motor-control/
out1 = 13
out2 = 11
out3 = 15
out4 = 12

actions = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
]
is_init = False

pins = [out1, out2, out3, out4]


def init_stepper():
    print("initiate pinout")
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    print("Reset GPIO stat")
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    is_init = True # to know if it been init or not


def move( spins=1,backward=False):
    if backward:
        act = actions[::-1]
    else:
        act = actions
        # one equal to 1.8
        # so this 7.2(1.8*4) (checked by try to see how many circle it do it 200 times (360/1.8 = 200))
        for i in range(50*spins):
            for motors_action in act:
                # print(motors_action) # for debug
                GPIO.output(out1, GPIO.HIGH if motors_action[0] else GPIO.LOW)
                GPIO.output(out2, GPIO.HIGH if motors_action[1] else GPIO.LOW)
                GPIO.output(out3, GPIO.HIGH if motors_action[2] else GPIO.LOW)
                GPIO.output(out4, GPIO.HIGH if motors_action[3] else GPIO.LOW)
                time.sleep(0.03)


if __name__ == '__main__':
    try:
        init_stepper()
        move()
    except:
        GPIO.cleanup()
    GPIO.cleanup()
