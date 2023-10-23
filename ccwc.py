#!/usr/bin/env python3

from src.wc import wc
import sys

wordcount = wc()

command_line_arguments = sys.argv

command_line_option = command_line_arguments[1]
command_line_file_path = command_line_arguments[2]

if command_line_option == '-c': 
    print(wordcount.read_bytes_from_file(command_line_file_path))
elif command_line_option == '-l':
    print(wordcount.read_lines_from_file(command_line_file_path))
else:
    print(f"Command line option -d is not supported")