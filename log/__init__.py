""" Logging config file"""
from os.path import dirname, abspath
from logging.config import fileConfig
import logging

LOG_DIR = dirname(dirname(abspath(__file__)))
CONFIG_FILE = LOG_DIR + '/log/logging_config.ini'
fileConfig(CONFIG_FILE)
LOGGER = logging.getLogger()


def log_info(info):
    """ logs informational messages"""
    LOGGER.info("Info : %s ", info)


def log_debug(info):
    """ logs debug messages"""
    LOGGER.debug("Debug : %s ", info)
