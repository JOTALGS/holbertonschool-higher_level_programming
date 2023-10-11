#!/usr/bin/python3


def main():
    """sdas"""
    ln = len(sys.argv) - 1
    if ln == 0:
        print("{} arguments.".fotmat(ln))
    elif ln == 1:
        print("{} argument:".format(ln))
    else:
        print("{} arguments:".format(ln))

    for i in range(1, ln + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    import sys
    main()
