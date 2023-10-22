import unittest
import subprocess

class TestCCWC(unittest.TestCase):
    
    def test_ccwc_returns_bytes_length_and_test_file_full_run(self):
        process = subprocess.Popen(["./ccwc.py", "-c", "text.txt"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), "335041 text.txt")

    def test_ccwc_returns_line_count_from_file_full_run(self):
        process = subprocess.Popen(["./ccwc.py", "-l", "text.txt"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), "7137 text.txt")