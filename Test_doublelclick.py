import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class TestActions:

    @pytest.fixture
    def setup(self):
        # Set up WebDriver (ensure chromedriver is in PATH or provide full path)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Open the webpage
        self.driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        # Yield the driver for use in test cases
        yield self.driver

        # Tear down - close and quit the driver after the test case completes
        time.sleep(3)
        self.driver.quit()

    def test_double_click(self, setup):
        driver = setup  # Access the driver from the fixture

        # Locate the double-click button using XPath
        double_click_button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")

        # Perform the double-click action
        actions = ActionChains(driver)
        actions.double_click(double_click_button).perform()

        # Wait for the alert to show up and accept it
        time.sleep(3)
        alert = driver.switch_to.alert
        alert.accept()

        # Wait to confirm the action worked
        time.sleep(2)
