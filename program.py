from digitalio import DigitalInOut, Direction, Pull
import board
import time

print("Starting Bag Controller")

ONBOARD_LED_PIN = board.GP25
RELAY_1_GPIO = board.GP6
RELAY_2_GPIO = board.GP7
RELAY_3_GPIO = board.GP8
RELAY_OPEN_SECONDS = 0.02
RELAY_DELAY_SECONDS = 15


def setup_output_pin(pin):
    output = DigitalInOut(pin)
    output.direction = Direction.OUTPUT
    return output


def setup_pins(pins):
    output_pins = []

    for pin in pins:
        output = setup_output_pin(pin)
        output_pins.append(output)

    return output_pins


onboard_led = setup_output_pin(ONBOARD_LED_PIN)

relays_pins = [RELAY_1_GPIO, RELAY_2_GPIO, RELAY_3_GPIO]
relays = setup_pins(relays_pins)


def print_status(relay_num, status, seconds):
    statusStr = "on" if status else "off"
    format_str = "Relay {relay_num} {status} ({seconds} seconds)"
    msg = format_str.format(relay_num=relay_num,
                            status=statusStr, seconds=seconds)
    print(msg)


def toggle_relay(relay):
    print_status(relay_number, True, RELAY_OPEN_SECONDS)

    relay.value = True
    time.sleep(RELAY_OPEN_SECONDS)

    print_status(relay_number, False, RELAY_DELAY_SECONDS)
    relay.value = False


while True:
    print("Starting Relay Sequence")

    relay_number = 1

    for relay in relays:
        onboard_led.value = True

        toggle_relay(relay)

        onboard_led.value = False
        time.sleep(RELAY_DELAY_SECONDS)
        relay_number += 1

    print("Finished Relay Sequence")
