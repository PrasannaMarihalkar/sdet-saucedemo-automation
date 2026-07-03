from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart_updates_badge(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_item_count() == 6

    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == "1"

def test_cart_navigation(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    assert "cart.html" in driver.current_url