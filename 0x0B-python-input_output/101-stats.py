#!/usr/bin/python3
"""Reads from stdin and computes metrics."""
import sys


file_size = 0
status_code = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
    "405": 0, "500": 0}

try:
    for line in sys.stdin:
        line = line.split()
        if len(line) > 2:
            status_code[line[-2]] += 1
        if len(line) > 0:
            file_size += int(line[-1])
except KeyboardInterrupt:
    pass

def print_stats():
    """Prints statistics."""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))
