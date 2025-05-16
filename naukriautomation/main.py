from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import traceback
import os

# === Configuration ===
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
RESUME_PATH = "Palantir_Foundry_Data_Engineer_Resume.pdf"  # Put your resume file in the repo root or use a relative path

# === Setup Chrome with headless mode ===
options = Options()
options.add_argument("--headless")  # run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    # 1. Open Naukri Login Page
    driver.get("https://www.naukri.com/nlogin/login")

    # 2. Enter Email and Password
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "usernameField"))
    ).send_keys(EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)

    # 3. Click Login Button
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    print("✅ Logged in successfully.")

    # 4. Go to profile
    view_profile_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/mnjuser/profile']"))
    )
    view_profile_link.click()
    print("✅ Clicked 'View profile' link.")

    # === Edit Basic Details ===
    try:
        edit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "em.icon.edit[data-ga-track*='EditProfile']"))
        )
        edit_button.click()
        print("✅ Clicked 'Edit Basic Details' icon.")

        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))  # Update if needed
        )
        name_field.clear()
        name_field.send_keys("Sandeep Revilla")
        print("✏️ Updated name field.")

        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "saveBasicDetailsBtn"))
        )
        save_button.click()
        print("💾 Clicked 'Save' to update basic details.")
    except Exception as e:
        print("⚠️ Could not update basic details. Skipping that step.")
        print(str(e))

    # === Upload Resume ===
    try:
        upload_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "attachCV"))  # Update this if needed
        )
        if os.path.exists(RESUME_PATH):
            upload_input.send_keys(os.path.abspath(RESUME_PATH))
            print("✅ Resume uploaded successfully.")
        else:
            print(f"❌ Resume file not found at: {RESUME_PATH}")
    except Exception as e:
        print("⚠️ Resume upload failed. Could not find upload field.")
        print(str(e))

except Exception as e:
    print("❌ Error occurred:", str(e))
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()
    print("🔚 Browser closed.")
