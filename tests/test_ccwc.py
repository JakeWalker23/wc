import unittest
import subprocess

class TestCCWC(unittest.TestCase):
    
    def test_ccwc_returns_bytes_length_and_test_file_full_run(self):
        process = subprocess.Popen(["./ccwc.py", "-c", "/Users/jake.walker/personal-development/wc/text.txt"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), "335041 /Users/jake.walker/personal-development/wc/text.txt")