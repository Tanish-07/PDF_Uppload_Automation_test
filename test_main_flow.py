import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# --- Page Object Class ---
class UploadPage:
    def __init__(self, driver):
        self.driver = driver
        self.upload_input = (By.ID, "file-upload")
        self.submit_button = (By.ID, "file-submit")
        self.success_message = (By.CSS_SELECTOR, "#content h3")

    def upload_file(self, file_path):
        self.driver.find_element(*self.upload_input).send_keys(file_path)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message_text(self):
        wait = WebDriverWait(self.driver, 10)
        message_element = wait.until(EC.visibility_of_element_located(self.success_message))
        return message_element.text


# --- Pytest Fixture ---
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# --- Test Function ---
def test_successful_upload(driver):
    driver.get("https://the-internet.herokuapp.com/upload")
    upload_page = UploadPage(driver)
    file_path = os.path.abspath("test_data/valid_document.pdf")

    upload_page.upload_file(file_path)
    upload_page.click_submit()

    success_text = upload_page.get_success_message_text()
    assert "File Uploaded!" in success_text