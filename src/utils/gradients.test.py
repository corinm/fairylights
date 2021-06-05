import unittest

from colour import Color

from utils.gradients import createGradientFromBlack, createGradientToBlack


class TestHelpers(unittest.TestCase):
    def test_works(self):
        steps = 5
        colours = createGradientFromBlack(Color("blue"), steps)
        self.assertEqual(len(colours), steps)
        self.assertEqual(
            colours,
            [
                Color("black"),
                Color("#000040"),
                Color("#00007f"),
                Color("#0000bf"),
                Color("blue"),
            ],
        )

    def test_works2(self):
        steps = 5
        colours = createGradientToBlack(Color("blue"), steps)
        self.assertEqual(len(colours), steps)
        self.assertEqual(
            colours,
            [
                Color("blue"),
                Color("#0000bf"),
                Color("#00007f"),
                Color("#000040"),
                Color("black"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
