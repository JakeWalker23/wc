from src.wc import wc
import unittest

class TestWC(unittest.TestCase):

    def test_read_bytes(self):
        wordcount = wc()
        string = 'jake'

        result = wordcount.read_bytes(string)

        self.assertEqual(result, 4)