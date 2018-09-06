import yaml
import logging.config
import os


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


def func():
    logger = logging.getLogger("my_module")
    logger.debug("start func")
    logger.info("exec func")
    logger.error("end func")


if __name__ == "__main__":
    setup_logging("../logging.yaml", "logs")
    func()
