from colour import Color

from colours.Colours import ColoursFromListOfPalettes
from .eighties import PINK, BLUE, GREEN

BLUE = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
GREEN = Color(rgb=(0 / 255, 70 / 255, 10 / 255))
RED = Color(rgb=(70 / 255, 0 / 255, 2 / 255))

GREEN_YELLOW = Color(rgb=(43 / 255, 70 / 255, 0 / 255))
GREEN_BLUE = Color(rgb=(6 / 255, 74 / 255, 33 / 255))


northernLights = ColoursFromListOfPalettes([
    [GREEN],
    [GREEN, GREEN_BLUE],
    [GREEN],
    [GREEN, GREEN_BLUE, BLUE],
    [GREEN, GREEN_BLUE, PINK],
    [GREEN, GREEN_BLUE],
    [GREEN],
    [GREEN, GREEN_BLUE, BLUE],
    [GREEN, GREEN_YELLOW],
    [GREEN, GREEN_YELLOW, RED],
    [GREEN, GREEN_YELLOW],
    [GREEN, GREEN_BLUE, BLUE],
    [GREEN, GREEN_BLUE, PINK],
    [PINK, GREEN_YELLOW],
    [GREEN],
])
