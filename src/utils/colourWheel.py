from colour import Color

RED = Color("#4c0000")
RED_ORANGE = Color("#4c0700")  # ff1a00
ORANGE = Color("#330d00")  # OrangeRed
ORANGE_YELLOW = Color("#4c3600")  # ff7400
YELLOW = Color("#484c00")  # Gold
YELLOW_GREEN = Color("#264c00")  # Chartreuse
GREEN = Color("#003300")  # Green
BLUE_GREEN = Color("#004c11")  # Cyan
BLUE = Color("#000066")  # Blue
BLUE_VIOLET = Color("#2a2452")  # SlateBlue
VIOLET = Color("#4f0835")  # MediumVioletRed
RED_VIOLET = Color("#4f0828")  # C71539


def maxSat(colour: Color) -> Color:
    colour.saturation = 1
    return colour


COLOUR_WHEEL = [
    maxSat(c)
    for c in [
        RED,
        RED_ORANGE,
        ORANGE,
        ORANGE_YELLOW,
        YELLOW,
        YELLOW_GREEN,
        GREEN,
        BLUE_GREEN,
        BLUE,
        BLUE_VIOLET,
        VIOLET,
        RED_VIOLET,
    ]
]
