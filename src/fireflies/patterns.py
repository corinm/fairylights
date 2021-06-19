from typing import Callable, Dict, List, Tuple

from colour import Color

from fireflies.FireflyColour import FireflyColour
from utils.colours import fireflies, off
from utils.gradients import createGradientFromBlack, createGradientToBlack


def staticGlow(
    ticksActive: int, colour: FireflyColour, steps: int = 10
) -> Callable[[], Tuple[Color, bool]]:
    state: int = 0

    up1 = createGradientFromBlack(fireflies["bright"], steps)
    down1 = createGradientToBlack(fireflies["bright"], steps)

    gradient: List[Color] = up1 + [fireflies["bright"] for _ in range(ticksActive)] + down1

    def tick() -> Tuple[Color, bool]:
        nonlocal state

        state += 1

        if state >= len(gradient):
            return (off, True)

        colour = gradient[state]

        return (colour, False)

    return tick


STEPS = 10

up1 = createGradientFromBlack(fireflies["bright"], STEPS)
down1 = createGradientToBlack(fireflies["bright"], STEPS)
gradient1: List[Color] = up1 + down1[1:]

up2 = createGradientFromBlack(fireflies["darker"], STEPS)
down2 = createGradientToBlack(fireflies["darker"], STEPS)
gradient2: List[Color] = up2 + down2[1:]

GRADIENT_LENGTH = STEPS * 2 - 1

gradients: Dict[FireflyColour, List[Color]] = {
    FireflyColour.BRIGHT: gradient1,
    FireflyColour.DARK: gradient2,
}

flickerGradient10: List[Color] = [
    up1[1],
    up1[1],
    up1[1],
    up1[2],
    up1[2],
    up1[3],
    up1[2],
    up1[1],
    up1[1],
    up1[1],
]

flickerGradient30: List[Color] = [
    up1[1],
    off,
    off,
    off,
    off,
    up1[2],
    up1[2],
    off,
    off,
    off,
    off,
    off,
    up1[1],
    up1[3],
    up1[5],
    up1[5],
    up1[5],
    fireflies["bright"],
    fireflies["bright"],
    up1[5],
    up1[5],
    up1[3],
    up1[3],
    up1[1],
    off,
    off,
    off,
    off,
    off,
    up1[1],
]


def flicker(ticksActive: int, colour: FireflyColour) -> Callable[[], Tuple[Color, bool]]:
    state: int = 0

    gradient: List[Color] = flickerGradient10 if ticksActive < 15 else flickerGradient30

    def tick() -> Tuple[Color, bool]:
        nonlocal state

        state += 1

        if state >= len(gradient):
            return (off, True)

        colour = gradient[state]

        return (colour, False)

    return tick
