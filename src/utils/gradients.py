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


def createGradientFromAndToBlack(colour: Color, stepsUp: int) -> List[Color]:
    up = createGradientFromBlack(colour, stepsUp)
    down = list(reversed(up))
    upAndDown: List[Color] = up + down[1:]
    return upAndDown
