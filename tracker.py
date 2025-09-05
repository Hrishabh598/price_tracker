from db import init_db, insert_price
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import time

def get_price(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    price = None
    try:
        priceDiv = driver.find_element(By.ID,"corePriceDisplay_desktop_feature_div")
        price = priceDiv.find_element(By.CLASS_NAME, "a-price-whole")
        print(price.text)
        if price:
            price = price.text.replace(",","").strip()

    finally:
        driver.quit()
    return price

    
def track(url, threshold):
    init_db()
    try:
        price = get_price(url)
        print(f"[INFO] Current price: {price}")
        insert_price(url,price)

        if price <= threshold:
            print(f"🔥 ALERT! Price dropped below {threshold}: {price}")
        else:
            print(f"✅ Price still above threshold: {price}")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    url = input("Enter product URL: ").strip()
    threshold = float(input("Enter price threshold:"))
    track(url, threshold)

