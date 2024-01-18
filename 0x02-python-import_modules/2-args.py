#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    argsCount = len(argv) - 1

    if argsCount == 1:
        print("{} argument.".format(argsCount))
    else:
        print("{} arguments.".format(argsCount))

    argsList = []
    for c in argv:
        argsList += [c]
    for i in range(1, len(argsList)):
        print("{} = {}".format(i, argsList[i]))
