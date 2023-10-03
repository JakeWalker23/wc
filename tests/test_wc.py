from src.wc import wc
import unittest

class TestWC(unittest.TestCase):

    def test_read_bytes_from_file(self):
        wordcount = wc()
        filepath = 'tests/data/text.txt'

        result = wordcount.read_bytes_from_file(filepath)

        self.assertEqual(result, 4) 