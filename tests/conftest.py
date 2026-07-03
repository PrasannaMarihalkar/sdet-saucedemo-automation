import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

pytest.saucedemo_headless = os.environ.get("CI") == "true"

@pytest.fixture
def driver():
    options = Options()
    if pytest.saucedemo_headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    if not pytest.saucedemo_headless:
        drv.maximize_window()
    yield drv
    drv.quit()
