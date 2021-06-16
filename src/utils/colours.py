from typing import Dict, List

from colour import Color

"""
   Retro colours e.g. Noma Pickwick fairy lights
"""
retroColours: Dict[str, Color] = {
    "pink": Color(rgb=(93 / 255, 19 / 255, 56 / 255)),
    "blue": Color(rgb=(11 / 255, 77 / 255, 57 / 255)),
    "orange": Color(rgb=(199 * 0.8 / 255, 90 * 0.8 / 255, 0 * 0.8 / 255)),
    "green": Color(rgb=(54 * 0.4 / 255, 139 / 255, 27 * 0.4 / 255)),
    "red": Color(rgb=(184 * 0.7 / 255, 44 * 0.4 / 255, 8 * 0.4 / 255)),
}

"""
   80s colours
"""
blue80s = Color(rgb=(11 / 255, 77 / 255, 57 / 255))
pink80s = Color(rgb=(57 / 255, 11 / 255, 77 / 255))

"""
   General
"""
off = Color(None)

"""
   Fireflies
   Original: rgb=(241 / 255, 250 / 255, 13 / 255)
"""
fireflies: Dict[str, Color] = {
    "bright": Color(rgb=(96 / 255, 100 / 255, 5 / 255)),
    "darker": Color(rgb=(38 / 255, 40 / 255, 2 / 255)),
}

"""
   Flickering fairy lights
"""
# 72,39,1 -> 145,90,3 is quite nice
_flicker2_4V = Color(rgb=(72 / 255, 32 / 255, 1 / 255))  # Dimmer
_flicker3V = Color(rgb=(145 / 255, 80 / 255, 3 / 255))  # Bright

flickerColours = list(_flicker3V.range_to(_flicker2_4V, 11))
flickerMid = flickerColours[5]  # For "DIM" flicker bulbs

# 263a01 - 38,58,1
# 282D00 - 40,45,0
# 262801 - rgb(38,40,1)


def process(colours: List[str]) -> List[Color]:
    c1 = ["#" + c for c in colours]
    c2 = [Color(c) for c in c1]
    for colour in c2:
        colour.luminance = 0.08
        colour.saturation = 1
    return c2


"""
   Colour palettes from coolors.co
"""
coolor1 = process(
    [
        "d9ed92",
        "b5e48c",
        "99d98c",
        "76c893",
        "52b69a",
        "34a0a4",
        "168aad",
        "1a759f",
        "1e6091",
        "184e77",
    ]
)

coolor2 = process(
    [
        "f72585",
        "b5179e",
        "7209b7",
        "560bad",
        "480ca8",
        "3a0ca3",
        "3f37c9",
        "4361ee",
        "4895ef",
        "4cc9f0",
    ]
)

coolor3 = process(["ffbe0b", "fb5607", "ff006e", "8338ec", "3a86ff"])

coolor4 = process(
    [
        "7400b8",
        "6930c3",
        "5e60ce",
        "5390d9",
        "4ea8de",
        "48bfe3",
        "56cfe1",
        "64dfdf",
        "72efdd",
        "80ffdb",
    ]
)

coolor5 = process(["9b5de5", "f15bb5", "fee440", "00bbf9", "00f567"])

coolor6 = process(
    [
        "b7094c",
        "a01a58",
        "892b64",
        "723c70",
        "5c4d7d",
        "455e89",
        "2e6f95",
        "1780a1",
        "0091ad",
    ]
)

coolor7 = process(["29bf12", "abff4f", "08bdbd", "f21b3f", "ff9914"])

coolor8 = process(["3d348b", "7678ed", "f7b801", "f18701", "f35b04"])

coolor9 = process(["f9c80e", "f86624", "ea3546", "662e9b", "43bccd"])

coolors = [
    coolor1,
    coolor2,
    coolor3,
    coolor4,
    coolor5,
    coolor6,
    coolor7,
    coolor8,
    coolor9,
]
