from src.wc import wc
import unittest

class TestWC(unittest.TestCase):
    def test_add_numbers(self):

        wordcount = wc()

        result = wordcount.add_numbers(2, 2)

        self.assertEqual(result, 4)