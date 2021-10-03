from colour import Color

from .Colours import ColoursFromListOfPalettes

PINK = Color(rgb=(57 / 255, 11 / 255, 77 / 255))
BLUE = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
GREEN = Color(rgb=(0 / 255, 70 / 255, 10 / 255))

PINK_BLUE = [PINK, BLUE]
PINK_BLUE_GREEN = [PINK, BLUE, GREEN]

eighties = ColoursFromListOfPalettes([PINK_BLUE, PINK_BLUE_GREEN])
