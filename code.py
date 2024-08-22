from digitalio import DigitalInOut, Direction, Pull
import board
import time

print("Starting Bag Controller")

THIRTY_SECONDS = 30;

# Number of seconds to open the relay
RELAY_OPEN_SECONDS = THIRTY_SECONDS
# Number of seconds between relays
RELAY_DELAY_SECONDS = THIRTY_SECONDS
# Number of relays to iterate
NUMBER_OF_RELAYS = 1
# Pin to check for power input
INPUT_PIN = board.GP1

ONBOARD_LED_PIN = board.GP25



# Pin mappings for Pico-relay B board
# Docs: https://www.waveshare.com/wiki/Pico-Relay-B
PICO_RELAY_B_PIN_CONFIG = [
    board.GP21,  # Channel 1
    board.GP20,  # Channel 2
    board.GP19,  # Channel 3
    board.GP18,  # Channel 4
    board.GP17,  # Channel 5
    board.GP16,  # Channel 6
    board.GP15,  # Channel 7
    board.GP14,  # Channel 8
]

# Set pin mapping
PIN_CONFIG = PICO_RELAY_B_PIN_CONFIG


def setup_output_pin(pin):
    output = DigitalInOut(pin)
    output.direction = Direction.OUTPUT
    return output


def setup_input_pin(pin):
    input_pin = DigitalInOut(pin)
    input_pin.direction = Direction.INPUT
    input_pin.pull = Pull.DOWN  # Use Pull.DOWN to detect high input
    return input_pin


def setup_pins(pins):
    output_pins = []

    for x in range(NUMBER_OF_RELAYS):
        pin = pins[x]
        output = setup_output_pin(pin)
        output_pins.append(output)

    return output_pins


onboard_led = setup_output_pin(ONBOARD_LED_PIN)
input_pin = setup_input_pin(INPUT_PIN)

relays = setup_pins(PIN_CONFIG)


def print_status(relay_num, status, seconds):
    status_str = "on" if status else "off"
    format_str = "Relay {relay_num} {status} ({seconds} seconds)"
    msg = format_str.format(relay_num=relay_num,
                            status=status_str, seconds=seconds)
    print(msg)


def toggle_relay(relay, relay_number):
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
    # Check if there's power on the input pin
    if input_pin.value:
        print("Power detected, starting Relay Sequence")

        relay_number = 1

        for relay in relays:
            onboard_led.value = False

            toggle_relay(relay, relay_number)

            onboard_led.value = False
            time.sleep(RELAY_DELAY_SECONDS)
            relay_number += 1

        print("Finished Relay Sequence")
    else:
        print("No power detected, skipping relay sequence")

    time.sleep(RELAY_DELAY_SECONDS)
