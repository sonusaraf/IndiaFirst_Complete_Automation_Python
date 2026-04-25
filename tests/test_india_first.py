import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def run_india_first_automation():
    # 1. Setup Chrome Options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment this to run without opening a window
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # 2. Initialize Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 15)

    try:
        print("Launching IndiaFirst Life Plan website...")
        driver.get("https://buyonline.indiafirstlife.com/term-plans/indiafirst-life-plan#/")

        # 3. Fill 'Your Full Name'
        # Using XPATH based on the label/placeholder structure
        name_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Your Full Name' or @name='fullName']")))
        name_input.send_keys("Sonu Kumar")
        print("Entered Name.")

        # 4. Select Date of Birth
        dob_input = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'DD/MM/YYYY')]")
        dob_input.send_keys("15/05/1995")
        print("Entered Date of Birth.")

        # 5. Fill Mobile Number
        mobile_input = driver.find_element(By.XPATH, "//input[@name='mobileNumber' or contains(@placeholder, 'Mobile')]")
        mobile_input.send_keys("9876543210")
        print("Entered Mobile Number.")

        # 6. Fill Email Address
        email_input = driver.find_element(By.XPATH, "//input[@name='emailAddress' or contains(@placeholder, 'Email')]")
        email_input.send_keys("sonu@gmail.com")
        print("Entered Email.")

        # 7. Select Gender (e.g., Male)
        male_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Male')]")
        male_option.click()
        print("Selected Gender.")

        # 8. Smoking Habits (e.g., No Smoking)
        smoking = driver.find_element(By.XPATH, "(//span[contains(text(), 'Smoking')])[1]")
        smoking.click()
        print("Selected Smoking Habit.")

        # 9. Click Continue
        continue_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]")
        # continue_btn.click() # Uncomment this when you are ready to proceed to the next page

        print("Automation Script Finished Successfully!")
        time.sleep(15)  # Pause to see the result

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_india_first_automation()