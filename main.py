from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import traceback
import time
from datetime import datetime

# === Configuration ===
EMAIL = "sandeeprevilla1999@gmail.com"
PASSWORD = "Sandeep@5872"

ERROR_LOG_FILE = "error_log.txt"

def log_error(error_message):
    with open(ERROR_LOG_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {error_message}\n\n")

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.naukri.com/nlogin/login")

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "usernameField"))
        ).send_keys(EMAIL)
    except Exception as e:
        driver.save_screenshot("error_usernameField.png")
        log_error(f"Failed to find 'usernameField': {str(e)}\n{traceback.format_exc()}")
        raise

    try:
        driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        print("✅ Logged in successfully.")
    except Exception as e:
        driver.save_screenshot("error_login.png")
        log_error(f"Login error: {str(e)}\n{traceback.format_exc()}")
        raise

except Exception as e:
    print(f"❌ Error during login: {e}")

finally:
    time.sleep(5)
    driver.quit()
    print("🔚 Browser closed.")
