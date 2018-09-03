#!/usr/bin/python3
import os


class IconPath:
    DIR = os.path.dirname(os.path.abspath(__file__))
    LEFT_ARROW = DIR + "\left-arrow.png"
    RIGHT_ARROW = DIR + "\\right-arrow.png"
    APPLICATION_ICON = DIR + "\\record.ico"
    CALC_ICON = DIR + "\writing.png"


def main():
    print(IconPath.DIR)
    print(IconPath.LEFT_ARROW)


if __name__ == "__main__":
    main()
