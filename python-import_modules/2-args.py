#!/usr/bin/python3
import sys
def main():
    ln = len(sys.argv) - 1
    if ln == 0:
        print("{} arguments:".fotmat(ln))
    elif ln == 1:
        print("{} argument:".format(ln))
    else:
        print("{} arguments:".format(ln))
    if ln > 0:
        for i in range(1,ln + 1):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
