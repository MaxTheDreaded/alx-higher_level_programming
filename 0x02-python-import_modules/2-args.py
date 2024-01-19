from sys import argv

if __name__ == "__main__":
    argsCount = len(argv) - 1

    if argsCount == 0:
        print("0 arguments.")
    elif argsCount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argsCount))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
