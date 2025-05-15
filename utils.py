# utils.py

from selenium import webdriver

def launch_browser(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver

def print_message(msg):
    print(f"[INFO] {msg}")

def get_credentials():
    return {
        "username": "Admin",
        "password": "admin123"
    }

def get_value_from_dict(data, key):
    return data.get(key, "Key not found")
