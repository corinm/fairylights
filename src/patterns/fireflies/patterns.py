# from typing import Callable, Dict, List, Tuple

# from colour import Color

# from patterns.fireflies.FireflyColour import FireflyColour
# from utils.colours import off
# from utils.gradients import createGradientFromAndToBlack


# def staticGlow(
#     ticksActive: int, colour: FireflyColour, steps: int = 10
# ) -> Callable[[], Tuple[Color, bool]]:
#     state: int = 0

#     c = fireflies["bright"].hex if colour == FireflyColour.BRIGHT else fireflies["darker"].hex

#     gradient: List[Color] = createGradientFromAndToBlack(c, steps)

#     def tick() -> Tuple[Color, bool]:
#         nonlocal state

#         state += 1

#         if state >= len(gradient):
#             return (off, True)

#         colour = gradient[state]

#         return (colour, False)

#     return tick


# STEPS = 10

# gradient1: List[Color] = createGradientFromAndToBlack(fireflies["bright"].hex, STEPS)
# gradient2: List[Color] = createGradientFromAndToBlack(fireflies["darker"].hex, STEPS)

# GRADIENT_LENGTH = STEPS * 2 - 1

# gradients: Dict[FireflyColour, List[Color]] = {
#     FireflyColour.BRIGHT: gradient1,
#     FireflyColour.DARK: gradient2,
# }


# def flatten(t):
#     return [item for sublist in t for item in sublist]


# flickerGradient10: List[Color] = flatten(
#     [
#         [c, c, c, c, c, c, c, c, c, c]
#         for c in [
#             gradient1[1],
#             gradient1[1],
#             gradient1[1],
#             gradient1[2],
#             gradient1[2],
#             gradient1[3],
#             gradient1[2],
#             gradient1[1],
#             gradient1[1],
#             gradient1[1],
#         ]
#     ]
# )

# flickerGradient30: List[Color] = flatten(
#     [
#         [c, c, c, c, c, c, c, c, c, c]
#         for c in [
#             gradient1[1],
#             off,
#             off,
#             off,
#             off,
#             gradient1[2],
#             gradient1[2],
#             off,
#             off,
#             off,
#             off,
#             off,
#             gradient1[1],
#             gradient1[3],
#             gradient1[5],
#             gradient1[5],
#             gradient1[5],
#             fireflies["bright"],
#             fireflies["bright"],
#             gradient1[5],
#             gradient1[5],
#             gradient1[3],
#             gradient1[3],
#             gradient1[1],
#             off,
#             off,
#             off,
#             off,
#             off,
#             gradient1[1],
#         ]
#     ]
# )


# def flicker(
#     ticksActive: int, colour: FireflyColour, steps: int = 10
# ) -> Callable[[], Tuple[Color, bool]]:
#     state: int = 0

#     gradient: List[Color] = flickerGradient10 if ticksActive < 15 else flickerGradient30

#     def tick() -> Tuple[Color, bool]:
#         nonlocal state

#         state += 1

#         if state >= len(gradient):
#             return (off, True)

#         colour = gradient[state]

#         return (colour, False)

#     return tick
