import json
from logging import getLogger, config
from command_sample.const import LOGGING_CONF

config_dict = None
with open(LOGGING_CONF, 'r', encoding='utf-8') as f:
    config_dict = json.load(f)

config.dictConfig(config_dict)
logger = getLogger(__name__)

def main():
    logger.debug(hello_user("test"))

def hello_user(user: str):
    return f"hello, {user}!"