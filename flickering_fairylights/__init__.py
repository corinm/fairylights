from .FlickeringFairyLights import FlickeringFairyLights


def run(leds):
    ff = FlickeringFairyLights()

    while True:
        leds.setLeds(ff.tick())
