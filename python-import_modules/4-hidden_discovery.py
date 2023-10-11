#!/usr/bin/python3


def main():
    """sdasd"""
    list = dir(hidden_4)
    for name in list:
        if not name.startswith("__"):
            print("{}".format(name))


if __name__ == "__main__":
    import hidden_4
    main()