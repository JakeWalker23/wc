#!/usr/bin/env python3

from src.wc import wc
import sys

wordcount = wc()

command_line_arguments = sys.argv

arg2 = command_line_arguments[2]

bytes = wordcount.read_bytes_from_file(arg2)

print(bytes)

