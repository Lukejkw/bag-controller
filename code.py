from digitalio import DigitalInOut, Direction, Pull
import board
import time

print("Starting Bag Controller")

# Number of seconds to open the relay
RELAY_OPEN_SECONDS = 0.04
# Number of seconds between relays
RELAY_DELAY_SECONDS = 7
# Number of relays to iterate
NUMBER_OF_RELAYS = 5

ONBOARD_LED_PIN = board.GP25

PIN_CONFIG = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    board.GP27,
    board.GP28
]


def setup_output_pin(pin):
    output = DigitalInOut(pin)
    output.direction = Direction.OUTPUT
    return output


def setup_pins(pins):
    output_pins = []

    for x in range(NUMBER_OF_RELAYS):
        pin = pins[x]
        output = setup_output_pin(pin)
        output_pins.append(output)

    return output_pins


onboard_led = setup_output_pin(ONBOARD_LED_PIN)

relays = setup_pins(PIN_CONFIG)


def print_status(relay_num, status, seconds):
    statusStr = "on" if status else "off"
    format_str = "Relay {relay_num} {status} ({seconds} seconds)"
    msg = format_str.format(relay_num=relay_num,
                            status=statusStr, seconds=seconds)
    print(msg)


def toggle_relay(relay):
    print_status(relay_number, True, RELAY_OPEN_SECONDS)

    relay.value = False
    time.sleep(RELAY_OPEN_SECONDS)

    print_status(relay_number, False, RELAY_DELAY_SECONDS)
    relay.value = True


# Turn off all relays
for relay in relays:
    relay.value = True

# Delay first run
time.sleep(RELAY_DELAY_SECONDS)

while True:
    print("Starting Relay Sequence")

    relay_number = 1

    for relay in relays:
        onboard_led.value = False

        toggle_relay(relay)

        onboard_led.value = False
        time.sleep(RELAY_DELAY_SECONDS)
        relay_number += 1

    print("Finished Relay Sequence")
