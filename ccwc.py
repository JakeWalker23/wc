#!/usr/bin/env python3

from src.wc import wc
import sys

wordcount = wc()

arguments = sys.argv

arg2 = arguments[2]

bytes = wordcount.read_bytes(arg2)

print(bytes)