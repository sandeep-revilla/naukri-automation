from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import time

# Set up Chrome with a unique user data dir to avoid session conflicts
options = Options()
options.add_argument("--headless")  # Optional: remove if you want to see the browser window
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Create a temporary user-data-dir to avoid session error
temp_dir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={temp_dir}")

# Launch the browser
driver = webdriver.Chrome(options=options)

try:
    # Open the Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")
    print("✅ Page loaded successfully:", driver.title)
    time.sleep(3)  # Optional: allow page to fully load
except Exception as e:
    print("❌ Failed to load the page:", e)
finally:
    driver.quit()
    print("🔚 Browser closed.")
