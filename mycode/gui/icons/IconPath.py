#!/usr/bin/python3
import os


class IconPath:
    TEST_PATH = os.path.dirname(os.path.abspath(__file__)) + "\left-arrow.png"

    def __init__(self):
        self.DIR = os.path.dirname(os.path.abspath(__file__))
        self.LEFT_ARROW = self.DIR + "\left-arrow.png"
        self.RIGHT_ARROW = self.DIR + "\\right-arrow.png"
        self.APPLICATION_ICON = self.DIR + "\\record.ico"
        self.CALC_ICON = self.DIR + "\writing.png"


def main():
    print(IconPath.DIR)
    print(IconPath.LEFT_ARROW)


if __name__ == "__main__":
    main()
