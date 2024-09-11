from config import settings
from apps.e2eui.e2eui_helper import E2EUIHelper
from selenium.webdriver.common.by import By
import random
import time

class E2EUI(E2EUIHelper):
    def __init__(self) -> None:
        super().__init__()
        self.__login = settings.E2E_LOGIN
        self.__password = settings.E2E_PASSWORD
        self.logger = settings.stream_logger
        self.url = settings.E3EUI_URL

    def __get_login(self):
        return self.__login
    
    def __get_password(self):
        return self.__password
    
    def auth(self):
        self.logger.info("Authentication")

        self.session.get(self.url)
        time.sleep(random.randrange(2, 5))
        
        assert self.has_css(selector="input#user-name"), "Undefined login form"
    
        self.logger.info("Fill username")
        self.action.move_to_element(self.session.find_element(By.ID, value="user-name")).perform()
        time.sleep(1)
        self.session.find_element(By.ID, value="user-name").send_keys(self.__get_login())
        time.sleep(1)

        assert self.has_css(selector="input#password"), "Undefined password form"
        
        self.logger.info("Fill password")
        self.action.move_to_element(self.session.find_element(By.ID, value="password")).perform()
        time.sleep(1)
        self.session.find_element(By.ID, value="password").send_keys(self.__get_password())
        time.sleep(1)

        assert self.has_css(selector="input#login-button"), "Undefined submit button"
        
        self.logger.info("Click submit")
        self.action.move_to_element(self.session.find_element(By.ID, value="login-button")).perform()
        time.sleep(1)
        self.session.find_element(By.ID, value="login-button").click()
        time.sleep(random.randrange(2, 5))

        assert self.has_css(selector="a.shopping_cart_link"), "Login failed"

    def add_to_cart(self):
        self.logger.info("Choose random item")
        item = random.choice(self.session.find_elements(By.CSS_SELECTOR, "div.inventory_item"))
        time.sleep(1)
        
        assert item is not None, "Failed choose random item"

        self.logger.info("Add to cart")
        item.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(random.randrange(1, 3))

        assert item.find_element(By.CSS_SELECTOR, "button").text == "Remove", "Failed add item to cart"

    def make_purchase(self):
        self.logger.info("Go to cart")
        self.session.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        time.sleep(random.randrange(1, 3))

        assert self.has_css(selector="div.cart_item"), "Failed to locate item in the cart"

        self.logger.info("Checkout")
        self.session.find_element(By.CSS_SELECTOR, "button#checkout").click()
        time.sleep(random.randrange(1, 3))

        self.logger.info("Fill first name")
        self.session.find_element(By.ID, value="first-name").send_keys("Aboba")
        time.sleep(1)

        self.logger.info("Fill last name")
        self.session.find_element(By.ID, value="last-name").send_keys("Abobin")
        time.sleep(1)

        self.logger.info("Fill ZIP code")
        self.session.find_element(By.ID, value="postal-code").send_keys("12345")
        time.sleep(1)

        self.logger.info("Continue")
        self.session.find_element(By.ID, value="continue").click()
        time.sleep(random.randrange(2, 5))

        self.logger.info("Finish purchase")
        self.session.find_element(By.ID, value="finish").click()
        time.sleep(random.randrange(2, 5))

        assert self.has_css(selector="div.complete-text"), "Failed to make the purchase"
        self.logger.info("Success")
