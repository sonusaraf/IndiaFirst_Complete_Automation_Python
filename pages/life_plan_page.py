from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LifePlanPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    # Specific Locators
    NAME_FIELD = (By.NAME, "fullName")
    DOB_FIELD = (By.XPATH, "//input[contains(@placeholder, 'DD/MM/YYYY')]")
    MOBILE_FIELD = (By.NAME, "mobileNumber")
    EMAIL_FIELD = (By.NAME, "emailAddress")
    FEMALE_RADIO = (By.XPATH, "//span[contains(text(), 'Female')]")
    SMOKING_RADIO = (By.XPATH, "//span[text()='Smoking']")
    CONTINUE_BTN = (By.XPATH, "//button[contains(text(), 'Continue')]")

    def fill_form(self, name, dob, mobile, email):
        self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*self.DOB_FIELD).send_keys(dob)
        self.driver.find_element(*self.MOBILE_FIELD).send_keys(mobile)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        
    def select_female_and_smoking(self):
        # Clicks specifically requested for Female and Smoking habits
        self.wait.until(EC.element_to_be_clickable(self.FEMALE_RADIO)).click()
        self.wait.until(EC.element_to_be_clickable(self.SMOKING_RADIO)).click()
