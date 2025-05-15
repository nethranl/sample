# test_login_demo.py

import time
import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_login_example():
    # Launch browser
    driver = utils.launch_browser("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    utils.print_message("Browser launched and site opened.")

    # Get credentials
    creds = utils.get_credentials()
    username = utils.get_value_from_dict(creds, "username")
    password = utils.get_value_from_dict(creds, "password")

    # Perform login
    utils.print_message(f"Trying to login with user: {username}")
    time.sleep(3)  # Wait for page to load

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()

    utils.print_message("Login button clicked.")
    time.sleep(4)

    # Perform logout
    try:
        utils.print_message("Attempting to log out...")
        # Click on profile icon (user dropdown)
        profile_icon = driver.find_element(By.CSS_SELECTOR, "img.oxd-userdropdown-img")
        profile_icon.click()
        time.sleep(2)

        # Click on the logout option
        logout_button = driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
        utils.print_message("Logout successful.")
    except Exception as e:
        utils.print_message(f"Logout failed: {e}")

    time.sleep(3)
    driver.quit()
