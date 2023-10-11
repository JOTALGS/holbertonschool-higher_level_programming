#!/usr/bin/python3


def main():
    """hhh"""
    argc = len(sys.argv)
    res = 0
    for i in range(1, argc):
        res += int(sys.argv(i))
    print("{}".format(res))


if __name__ == "__main__":
    import sys
    main()
