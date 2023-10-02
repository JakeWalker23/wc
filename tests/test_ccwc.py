import unittest
import subprocess

class TestCCWC(unittest.TestCase):
    
    def test_string_passed_as_argument_returns_bytes_length(self):

        process = subprocess.Popen(["./ccwc.py", "-c", "jake"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), '4')

    
    def test_string_passed_as_argument_returns_bytes_length_2(self):

        process = subprocess.Popen(["./ccwc.py", "-c", "letter"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), '6')

    def test_text_file_passed_as_argument_returns_bytes_length(self):

        process = subprocess.Popen(["./ccwc.py", "-c", "text.txt"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), '4')