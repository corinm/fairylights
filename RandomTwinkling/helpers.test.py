import unittest

import helpers
import random
import collections


class TestHelpers(unittest.TestCase):
    def test_generates_a_list_of_50_bulbs(self):
        shuffled = helpers.createShuffledList(50, random)
        self.assertEqual(len(shuffled), 50)

    def test_list_is_evenly_shuffled(self):
        random.seed(1)
        shuffled = helpers.createShuffledList(50, random)

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
        shuffled = helpers.createShuffledList(50, random)

        # 0-5 contain one number between 0 and 9, one between 10 and 19 etc.
        counter = collections.Counter(shuffled)

        for i in range(50):
            self.assertEqual(counter.get(i), 1)

    def test_generates_new_list_each_time(self):
        random.seed(1)
        shuffled1 = helpers.createShuffledList(50, random)
        shuffled2 = helpers.createShuffledList(50, random)

        self.assertNotEqual(shuffled1, shuffled2)


if __name__ == '__main__':
    unittest.main()
