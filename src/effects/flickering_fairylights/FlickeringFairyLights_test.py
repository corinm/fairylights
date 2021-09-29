import unittest

import effects.flickering_fairylights.helpers as helpers
from effects.flickering_fairylights.FlickerBulb import BulbState
from utils.colours import _flicker2_4V, _flicker3V, flickerColours, off


class TestFlickeringFairyLight(unittest.TestCase):
    def test_all_flicker_bulbs_on_returns_all_24V(self):
        colours = helpers.generateFullListOfColours([BulbState.ON for i in range(10)])
        self.assertEqual(len(colours), 50)

        for i in range(50):
            self.assertEqual(colours[i], _flicker2_4V)

    def test_all_flicker_bulbs_off_returns_all_3V_except_flicker_bulbs(self):
        colours = helpers.generateFullListOfColours([BulbState.OFF for i in range(10)])
        self.assertEqual(len(colours), 50)

        for i in range(50):
            if i % 5 == 0:
                self.assertEqual(colours[i], off)
            else:
                self.assertEqual(colours[i], _flicker3V)

    def test_bulbs_are_correct_colours_1ON_1DIM(self):
        colours = helpers.generateFullListOfColours(
            [
                BulbState.ON,
                BulbState.DIM,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
            ]
        )
        self.assertEqual(len(colours), 50)

        for i in range(50):
            if i == 0:
                self.assertEqual(colours[i], flickerColours[1])
            elif i == 5:
                self.assertEqual(colours[i], flickerColours[5])
            elif i % 5 == 0:
                self.assertEqual(colours[i], off)
            else:
                self.assertEqual(colours[i], flickerColours[1])

    def test_bulbs_are_correct_colours_1ON_2DIM(self):
        colours = helpers.generateFullListOfColours(
            [
                BulbState.ON,
                BulbState.DIM,
                BulbState.DIM,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
                BulbState.OFF,
            ]
        )
        self.assertEqual(len(colours), 50)

        for i in range(50):
            if i == 0:
                self.assertEqual(colours[i], flickerColours[2])
            elif i == 5 or i == 10:
                self.assertEqual(colours[i], flickerColours[5])
            elif i % 5 == 0:
                self.assertEqual(colours[i], off)
            else:
                self.assertEqual(colours[i], flickerColours[2])


if __name__ == "__main__":
    unittest.main()
