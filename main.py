# main.py
import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    driver = uc.Chrome(options=options)
    driver.get("https://www.naukri.com/")
    print("✅ Page loaded successfully:", driver.title)
except Exception as e:
    print("❌ Failed to load page:", e)
finally:
    driver.quit()
