from fireflies.Fireflies import Fireflies


def run(leds):
    ff = Fireflies(50)

    while True:
        leds.setLeds(ff.tick())
