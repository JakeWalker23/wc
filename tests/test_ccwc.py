import unittest
import subprocess

class TestCCWC(unittest.TestCase):
    
    def test_text_file_passed_as_argument_returns_bytes_length(self):

        process = subprocess.Popen(["./ccwc.py", "-c", "/Users/jake.walker/personal-development/wc/tests/data/text.txt"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), '4')
    
    def test_ccwc_returns_bytes_length_and_test_file_full_run(self):
        process = subprocess.Popen(["./ccwc.py", "-c", "/Users/jake.walker/personal-development/wc/test.txt"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), "341836 test.txt")