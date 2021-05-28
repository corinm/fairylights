import unittest

from FlickerBulb import BulbState
from FlickeringFairyLights import generateFullListOfColours
import ledColours


class TestFlickeringFairyLight(unittest.TestCase):
    def test_tbc(self):
        colours = generateFullListOfColours([BulbState.ON, BulbState.DIM, BulbState.OFF, BulbState.OFF,
                                            BulbState.OFF, BulbState.OFF, BulbState.OFF, BulbState.OFF, BulbState.OFF, BulbState.OFF])
        self.assertEqual(len(colours), 50)
        self.assertEqual(colours, [])


if __name__ == '__main__':
    unittest.main()
