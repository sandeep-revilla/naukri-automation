from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback
import os

# === Configuration ===
EMAIL = sandeeprevilla1999@gmail.com
PASSWORD = Sandeep@5872
RESUME_PATH = os.path.join(os.getcwd(), resume.pdf)  # Keep this file in same folder

# === Setup Chrome for cloud ===
options = Options()
options.add_argument(--headless)
options.add_argument(--no-sandbox)
options.add_argument(--disable-dev-shm-usage)
options.add_argument(--window-size=1920,1080)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try
    driver.get(httpswww.naukri.comnloginlogin)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, usernameField))).send_keys(EMAIL)
    driver.find_element(By.ID, passwordField).send_keys(PASSWORD)
    driver.find_element(By.XPATH, button[text()='Login']).click()
    print(✅ Logged in successfully.)

    view_profile_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, a[@href='mnjuserprofile']))
    )
    view_profile_link.click()
    print(✅ Clicked 'View profile' link.)

    # Optional Edit basic details
    try
        edit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, em.icon.edit[data-ga-track='EditProfile']))
        )
        edit_button.click()
        print(✅ Clicked 'Edit Basic Details' icon.)

        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, name))
        )
        name_field.clear()
        name_field.send_keys(Sandeep Revilla)
        print(✏️ Updated name field.)

        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, saveBasicDetailsBtn))
        )
        save_button.click()
        print(💾 Clicked 'Save' to update basic details.)
    except
        print(⚠️ Skipping basic details update – not available.)

    # Resume Upload
    upload_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, attachCV))
    )

    if os.path.exists(RESUME_PATH)
        upload_input.send_keys(RESUME_PATH)
        print(✅ Resume uploaded successfully.)
    else
        print(f❌ Resume file not found at {RESUME_PATH})

except Exception as e
    print(❌ Error occurred, str(e))
    traceback.print_exc()

finally
    time.sleep(5)
    driver.quit()
    print(🔚 Browser closed.)
