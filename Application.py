#!/usr/bin/python3
import yaml
import logging.config
import logging
import os

from mycode.gui.controller.MainPageController import *


class Application:

    def start(self):
        logger = logging.getLogger()
        logger.info("Calculator start")
        MainPageController().openMainPage()


def setup_logging(configPath, storeDir, default_level=logging.INFO, env_key="LOG_CFG"):
    if not os.path.exists(storeDir):
        os.mkdir(storeDir)

    value = os.getenv(env_key, None)
    if value:
        configPath = value
    if os.path.exists(configPath):
        with open(configPath, "r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def main():
    setup_logging("mycode/logging.yaml", "logs")
    Application().start()


if __name__ == '__main__':
    main()
