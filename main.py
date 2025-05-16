from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Setup Chrome options (non-headless for debugging)
options = Options()
# options.add_argument("--headless")  # comment out for now to see browser window

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.naukri.com/nlogin/login")

    # Wait up to 20 seconds for the email input to appear
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "usernameField"))
    )
    print("✅ Login page loaded and email field found!")

except Exception as e:
    print("❌ Error loading login page or finding element:", e)

finally:
    driver.quit()
