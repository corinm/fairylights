from typing import Callable, Dict, List, Tuple

from colour import Color

from fireflies.FireflyColour import FireflyColour
from utils.colours import fireflies, off
from utils.gradients import createGradientFromBlack, createGradientToBlack

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


def staticGlow(
    ticksActive: int, colour: FireflyColour
) -> Callable[[], Tuple[Color, bool]]:
    state: int = 0

    gradient: List[Color] = (
        up1 + [fireflies["bright"] for _ in range(ticksActive)] + down1
    )

    def tick() -> Tuple[Color, bool]:
        nonlocal state

        state += 1

        if state >= len(gradient):
            return (off, True)

        colour = gradient[state]

        return (colour, False)

    return tick
