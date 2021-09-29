from enum import Enum
from typing import Dict

from colour import Color


class FireflyColour(Enum):
    BRIGHT = 1
    DARK = 2


"""
   Fireflies
   Original: rgb=(241 / 255, 250 / 255, 13 / 255)
"""
colours: Dict[FireflyColour, Color] = {
    FireflyColour.BRIGHT: Color(rgb=(96 / 255, 100 / 255, 5 / 255)),
    FireflyColour.DARK: Color(rgb=(38 / 255, 40 / 255, 2 / 255)),
}
