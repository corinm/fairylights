import functools
from typing import List

from colour import Color


def createGradientFromBlack(colour: Color, steps: int) -> List[Color]:
    rangeOfLuminosities = [(i / (steps - 1)) * colour.luminance for i in range(steps)]

    rangeOfColours = []
    for lum in rangeOfLuminosities:
        newColour = Color(colour)
        newColour.luminance = lum
        rangeOfColours.append(newColour)

    return rangeOfColours


def createGradientToBlack(colour: Color, steps: int) -> List[Color]:
    return list(reversed(createGradientFromBlack(colour, steps)))


def colourToHexString(function):
    def wrapper(*args):
        args = [x.hex if type(x) == Color else x for x in args]
        result = function(*args)
        return result

    return wrapper


@functools.lru_cache()
def createGradientFromAndToBlack(hex: str, stepsUp: int) -> List[Color]:
    colour = Color(hex)
    up = createGradientFromBlack(colour, stepsUp)
    down = list(reversed(up))
    upAndDown: List[Color] = up + down[1:]
    return upAndDown
