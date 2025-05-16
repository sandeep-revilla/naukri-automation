import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

try:
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")  # Use old "--headless" if needed
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = uc.Chrome(options=options)

    url = "https://www.naukri.com"  # or the actual login page if needed
    driver.get(url)

    print(f"✅ Page loaded successfully: {driver.title}")
except Exception as e:
    print(f"❌ Error loading page: {e}")
finally:
    driver.quit()
    print("🔚 Browser closed.")
