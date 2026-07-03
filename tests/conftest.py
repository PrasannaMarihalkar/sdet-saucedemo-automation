import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()
    yield drv
    drv.quit()