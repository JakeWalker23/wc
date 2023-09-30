import unittest
import subprocess

class TestCCWC(unittest.TestCase):
    
    def test_read_arguments_from_terminal(self):

        process = subprocess.Popen(["./ccwc.py", "-c", "jake"], stdout=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.assertEqual(stdout, 4)