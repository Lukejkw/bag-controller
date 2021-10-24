# Bag Controller

Firmware to automatically turn on/off relays for a bag controller.

## Settings

The following settings can be changed to control the timings and pins of the bag controller

```py
ONBOARD_LED_PIN = board.GP25
RELAY_1_GPIO = board.GP6
RELAY_2_GPIO = board.GP7
RELAY_3_GPIO = board.GP9
RELAY_OPEN_SECONDS = 0.02
RELAY_DELAY_SECONDS = 15
```

Relay Order Reference:

```py
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
```

## Pin Out Reference

<img src="https://content.instructables.com/ORIG/F9P/NT4Y/KQV84JVH/F9PNT4YKQV84JVH.jpg?auto=webp&frame=1&fit=bounds&md=0272bc9dda9fafa6bf0e138cbaa910a4">

[Source](https://www.instructables.com/Raspberry-Pi-Pico-Getting-Started-on-Board-Blink-L/)
