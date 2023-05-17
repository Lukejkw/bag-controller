# Bag Controller

Firmware to automatically turn on/off relays for a bag controller.

## Settings

The following settings can be changed to control the timings and pins of the bag controller

```py
RELAY_OPEN_SECONDS = 0.02
RELAY_DELAY_SECONDS = 15
```

## Relay Order Reference:

### Normal Mode

```py
PIN_CONFIG = [
    board.GP0, # Relay 1
    board.GP1, # Relay 2
    board.GP2, # Relay 3
    board.GP3, # Relay n ...
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

### Pico-relay B

> Please note that only 8 relays/channels are supported with pico relay B

```py
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
```

## Pin Out Reference

<img src="https://content.instructables.com/ORIG/F9P/NT4Y/KQV84JVH/F9PNT4YKQV84JVH.jpg?auto=webp&frame=1&fit=bounds&md=0272bc9dda9fafa6bf0e138cbaa910a4">

[Source](https://www.instructables.com/Raspberry-Pi-Pico-Getting-Started-on-Board-Blink-L/)


