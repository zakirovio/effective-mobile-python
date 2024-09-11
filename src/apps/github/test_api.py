from config.settings import stream_logger as logger, GITHUB_REPO, GITHUB_USERNAME, GITHUB_API_HEADERS
import requests
import time

def create_repo():
    logger.info("Create new repo")

    body = {
        "name": GITHUB_REPO,
        "description": "This is a test repository created via API",
        "private": False
    }

    resp = requests.post("https://api.github.com/user/repos", json=body, headers=GITHUB_API_HEADERS)
    time.sleep(1)

    logger.info(resp.status_code)
    logger.debug(resp.json())

    assert resp.status_code in [200, 201], "Bad status code"
    assert resp.json().get("full_name") == f"{GITHUB_USERNAME}/{GITHUB_REPO}" and not resp.json().get("private"), "Failed create a new private repo"
    
    logger.info("Success")

def check_repos():
    logger.info("Get all user repos")

    resp = requests.get("https://api.github.com/user/repos", headers=GITHUB_API_HEADERS)
    time.sleep(1)

    logger.info(resp.status_code)
    logger.debug(resp.json())
    logger.debug(f"Objects count: {len(resp.json())}")

    assert resp.status_code == 200, "Bad status code"
    assert resp.json()[-1].get("name") == GITHUB_REPO, "Failed find new repo in repos list"

    logger.info("Success")

def delete_repo():
    logger.info("Delete specified user repo")

    resp = requests.delete(f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}", headers=GITHUB_API_HEADERS)
    time.sleep(1)

    logger.info(resp.status_code)

    assert resp.status_code == 204, "Bad status code. Failed delete user repo"

    logger.info("Success")

def main() -> None:
    create_repo()
    check_repos()
    delete_repo()
