#!/usr/bin/python3
import sys
if __name__ == "__main":
    args = sys.argv[1:]  # Get all command-line arguments except the script name itself
    count = 0
    for arg in args:
        count += int(arg)
    print(count)
