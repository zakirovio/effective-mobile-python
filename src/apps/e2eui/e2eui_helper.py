from config import settings
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class E2EUIHelper:
    def __init__(self) -> None:
        self.session = self.create_session()
        self.action = ActionChains(self.session)

    def create_session(self) -> webdriver:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=settings.options)
    
    def has_css(self, selector: str, text: str | None = None, wait: int = 15) -> bool:
        try:
            element = WebDriverWait(self.session, wait).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )
            return True
        except TimeoutException:
            return False
