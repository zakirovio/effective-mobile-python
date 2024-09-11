from apps.e2eui.test_e2eui import main as e2eui
from apps.github.test_api import main as github
from config import settings
from sys import argv

util, param = argv

def undefined_param():
    settings.stream_logger.error(msg="Undefined parameter")

command_map = {
    "e2eui": e2eui,
    "github": github
}

if __name__ == '__main__':
    assert util == "run.py", settings.stream_logger.error(msg="Undefined utility. Use: python run.py <param>")
    command_map.get(param, undefined_param)()
