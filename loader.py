import RPIO
import time
import datetime

print("loader.py started")

RPIO.setmode(RPIO.BOARD)

RPIO.setup(11, RPIO.IN) # Pull down resistor connected to ground
RPIO.setup(16, RPIO.OUT)

# blinking function
def blink(pin):
        RPIO.output(pin, RPIO.HIGH)
        time.sleep(0.1)
        RPIO.output(pin, RPIO.LOW)
        time.sleep(0.1)
        # RPIO.output(pin, RPIO.HIGH)
        return

pushCounter = 0
lastState = False
buttonState = False
lastEvent = datetime.datetime.now()

print("loader.py ready")

try:
    while True:
        buttonState = RPIO.input(11)
        if buttonState != lastState:
            if buttonState:
                pushCounter += 1
                time.sleep(0.17)
                lastEvent = datetime.datetime.now()
        lastState = buttonState
        if pushCounter > 0 and (datetime.datetime.now() - lastEvent).seconds > 1:
            print("Button pressed", pushCounter, "times.")
            pushCounter = 0

except (KeyboardInterrupt, SystemExit):
    print("Goodbye!")
finally:
    RPIO.cleanup()
