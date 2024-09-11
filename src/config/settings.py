from decouple import Config, RepositoryEnv
import logging.config
from pathlib import Path
from selenium.webdriver import ChromeOptions

BASE_DIR = Path(__file__).resolve().parent.parent
config = Config(RepositoryEnv(f"{BASE_DIR}/.env"))

# Chrome driver settings
options = ChromeOptions()

options.add_argument('--ignore-ssl-errors')
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-extensions")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-popup-blocking")

# Logging config
log_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "[%(levelname)s]: %(asctime)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "streamLogger": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": "no"
        }
    }
}

# Loggers
logging.config.dictConfig(log_config)
stream_logger = logging.getLogger("streamLogger")

# E2EUI settings
E3EUI_URL = "https://www.saucedemo.com"
E2E_LOGIN = config("E2E_LOGIN")
E2E_PASSWORD = config("E2E_PASSWORD")

# Github settings
GITHUB_TOKEN = config("GITHUB_TOKEN") # Personal access token (classic)
GITHUB_REPO = config("GITHUB_REPO")
GITHUB_USERNAME = config("GITHUB_USERNAME")

GITHUB_API_HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}
