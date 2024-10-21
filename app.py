from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Firefox ke liye options set karna (headless mode agar chahiye toh)
options = Options()
# options.headless = True  # Is line ko uncomment karein agar aap headless mode mein run karna chahte hain

# GeckoDriver ka service create karna
service = Service('/usr/local/bin/geckodriver')

# WebDriver create karna
driver = webdriver.Firefox(service=service, options=options)

try:
    # YouTube website ko open karna
    driver.get("https://youtube.com")
    
    # Thoda wait karna taaki page load ho sake
    time.sleep(3)

    # Title ko print karna
    print("Page Title:", driver.title)
finally:
    # Browser ko close karna
    driver.quit()
