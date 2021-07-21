import collections
import random
import unittest

import random_twinkling.helpers as helpers


class TestHelpersCreateShuffledList(unittest.TestCase):
    def test_generates_a_list_of_50_bulbs(self):
        shuffled = helpers.createShuffledList(50)
        self.assertEqual(len(shuffled), 50)

    def test_list_is_evenly_shuffled(self):
        random.seed(1)
        shuffled = helpers.createShuffledList(50)

        # 0-5 contain one number between 0 and 9, one between 10 and 19 etc.
        divided = map(lambda x: int(x / 10), shuffled[0:5])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[5:10])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[10:15])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[15:20])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[20:25])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[25:30])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[30:35])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[35:40])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[40:45])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

        divided = map(lambda x: int(x / 10), shuffled[45:50])
        counter = collections.Counter(divided)
        self.assertEqual(counter.get(0), 1)
        self.assertEqual(counter.get(1), 1)
        self.assertEqual(counter.get(2), 1)
        self.assertEqual(counter.get(3), 1)
        self.assertEqual(counter.get(4), 1)

    def test_every_number_appears_once(self):
        random.seed(1)
        shuffled = helpers.createShuffledList(50)

        # 0-5 contain one number between 0 and 9, one between 10 and 19 etc.
        counter = collections.Counter(shuffled)

        for i in range(50):
            self.assertEqual(counter.get(i), 1)

    def test_generates_new_list_each_time(self):
        random.seed(1)
        shuffled1 = helpers.createShuffledList(50)
        shuffled2 = helpers.createShuffledList(50)

        self.assertNotEqual(shuffled1, shuffled2)


class TestHelpersCalculateLuminance(unittest.TestCase):
    def test_1(self):
        time = 0
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0)

    def test_2(self):
        time = 0.25
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0.0375)

    def test_3(self):
        time = 0.5
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0.075)

    def test_4(self):
        time = 0.75
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0.1125)

    def test_5(self):
        time = 1
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0.15)

    def test_6(self):
        time = 1.25
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0.1125)

    def test_7(self):
        time = 1.5
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0.075)

    def test_8(self):
        time = 1.75
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0.0375)

    def test_9(self):
        time = 2
        timeToPeak = 1
        maxLuminance = 0.15
        self.assertEqual(helpers.calculateLuminance(time, timeToPeak, maxLuminance), 0)


if __name__ == "__main__":
    unittest.main()
