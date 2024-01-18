#!/usr/bin/python3
from sys import argv
from unittest import result

if __name__ == "__main__":

    args = []

    for n in argv:
        args.append(n)

    result = 0
    for i in range(1, len(args)):
        result += int(args[i])

    print("{}".format(result))
