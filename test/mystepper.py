import RPi.GPIO as GPIO
import time

out1 = 13
out2 = 11
out3 = 15
out4 = 12

pins = [out1, out2, out3, out4]

print("initiate pinout")
GPIO.setmode(GPIO.BOARD)
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

print("Reset GPIO stat")
for pin in pins:
    GPIO.output(pin, GPIO.LOW)

# actions = [
#     [0,  1,  1,  0,  1, ],
#     [0,  1,  0,  0,  1, ],
#     [0,  1,  0,  1,  1, ],
#     [0,  1,  0,  1,  0, ],
#     [1,  1,  0,  1,  0, ],
#     [1,  0,  0,  1,  0, ],
#     [1,  0,  1,  1,  0, ],
#     [1,  0,  1,  0,  0, ],
#     [1,  0,  1,  0,  1, ],
#     [0,  0,  1,  0,  1, ],
# ]
print("write the way it go")
actions = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
]
try:

    print("start working")
    while 1:
        # i = input()
        # motors_action = bin(int(i, 16))[2:].zfill(4)
        for motors_action in actions[::-1]:
            print(motors_action)
            GPIO.output(out1, GPIO.HIGH if motors_action[0] else GPIO.LOW)
            GPIO.output(out2, GPIO.HIGH if motors_action[1] else GPIO.LOW)
            GPIO.output(out3, GPIO.HIGH if motors_action[2] else GPIO.LOW)
            GPIO.output(out4, GPIO.HIGH if motors_action[3] else GPIO.LOW)
            time.sleep(0.03)

except:
    print('clean up after error')
    GPIO.cleanup()

print('clean up')
GPIO.cleanup()
