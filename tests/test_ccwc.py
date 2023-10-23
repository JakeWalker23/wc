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

        self.assertEqual(stdout.strip(), "7144 text.txt")

    def test_command_line_option_displays_error_message_for_unknown_option(self):
        process = subprocess.Popen(["./ccwc.py", "-d", "text.txt"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout.strip(), "Command line option -d is not supported")