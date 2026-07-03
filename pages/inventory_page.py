from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class InventoryPage:
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        self.driver = driver

    def add_first_item_to_cart(self):
        self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)[0].click()

    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("cart.html"))

    def get_item_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))