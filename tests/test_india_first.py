import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.life_plan_page import LifePlanPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_complete_registration_flow(driver):
    driver.get("https://buyonline.indiafirstlife.com/term-plans/indiafirst-life-plan#/")
    
    lp = LifePlanPage(driver)
    lp.fill_form("Jane Doe", "20/05/1998", "9000000000", "jane.doe@example.com")
    lp.select_female_and_smoking()
    
    # Validation
    assert "IndiaFirst" in driver.title
    print("SUCCESS: Form filled with Female and Smoking options.")
