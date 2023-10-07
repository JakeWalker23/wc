from src.wc import wc
import unittest

class TestWC(unittest.TestCase):

    def test_read_bytes_from_file(self):
        wordcount = wc()
        filepath = 'tests/data/text.txt'

        result = wordcount.read_bytes_from_file(filepath)

        self.assertEqual(result, "4 tests/data/text.txt") 

    def test_fileNotFound_exception_raised_when_file_does_not_exist(self):
        wordcount = wc()
        filepath = 'does/not/exist.txt'

        with self.assertRaises(FileNotFoundError):
            wordcount.read_bytes_from_file(filepath)
    
    def test_read_lines_from_file(self, filepath):
        wordcount = wc()
        filepath = 'tests/data/text.txt'

        result = wordcount.read_lines_from_file(filepath)

        self.assertEqual(result, "1 tests/data/text.txt")
