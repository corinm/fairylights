from colour import Color

off = Color(rgb=(0, 0, 0))
flicker3V = Color(rgb=(100/255, 100/255, 100/255))
flicker2_4V = Color(rgb=(50/255, 50/255, 50/255))

flickerColours = list(flicker2_4V.range_to(flicker3V, 11))
