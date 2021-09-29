import unittest

import effects.flickering_fairylights.constants as constants
from effects.flickering_fairylights.FlickerBulb import BulbState, FlickerBulb


class TestFlickerBulb(unittest.TestCase):
    def test_starts_dim_with_temp_zero_then_on(self):
        fb = FlickerBulb()

        self.assertEqual(fb.temp, 0)
        self.assertEqual(fb.state, BulbState.DIM)
        fb.tick()
        self.assertEqual(fb.state, BulbState.ON)

    def test_does_not_heat_up_while_dim(self):
        fb = FlickerBulb(1)

        self.assertEqual(fb.state, BulbState.DIM)
        self.assertEqual(fb.temp, 0)
        fb.tick()
        self.assertEqual(fb.temp, 0)

    def test_turns_off_when_hot(self):
        fb = FlickerBulb(1)
        fb.temp = constants.OFF_TEMP - 1
        fb.state = BulbState.ON

        fb.tick()

        self.assertEqual(fb.temp, 100)
        self.assertEqual(fb.state, BulbState.DIM)
        fb.tick()
        self.assertEqual(fb.state, BulbState.OFF)

    def test_does_not_cool_when_dim(self):
        fb = FlickerBulb(1)
        fb.temp = 101
        fb.state = BulbState.DIM

        fb.tick()

        self.assertEqual(fb.state, BulbState.OFF)
        self.assertEqual(fb.temp, 101)

    def test_turns_back_on_when_cooled(self):
        fb = FlickerBulb(1)
        fb.temp = constants.ON_TEMP + 1
        fb.state = BulbState.OFF

        fb.tick()

        self.assertEqual(fb.temp, 90)
        self.assertEqual(fb.state, BulbState.DIM)
        fb.tick()
        self.assertEqual(fb.state, BulbState.ON)


if __name__ == "__main__":
    unittest.main()
