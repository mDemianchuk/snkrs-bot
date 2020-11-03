import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT_THRESHOLD = 3


class WebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=self.__get_chromedriver_path(), options=self.__get_options())
        # self.driver.maximize_window()

    def __get_chromedriver_path(self):
        current_dir_path = os.path.dirname(__file__)
        chromedriver_path = os.path.join(current_dir_path, "chromedriver")
        # for Windows users
        if os.name == "nt":
            chromedriver_path += ".exe"
        return chromedriver_path

    def __get_options(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return options

    def __find_element_by_element_selector(self, element_selector):
        try:
            return WebDriverWait(self.driver, TIMEOUT_THRESHOLD).until(
                EC.visibility_of_element_located(element_selector)
            )
        except TimeoutException:
            logging.warning(f"Element isn't located yet: {element_selector}")

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def find_element_by_class(self, class_name):
        return self.__find_element_by_element_selector((By.CLASS_NAME, class_name))

    def find_element_by_css_selector(self, css_selector):
        return self.__find_element_by_element_selector((By.CSS_SELECTOR, css_selector))

    def find_element_by_name(self, element_name):
        return self.__find_element_by_element_selector((By.NAME, element_name))

    def find_element_by_x_path(self, element_x_path):
        return self.__find_element_by_element_selector((By.XPATH, element_x_path))

    def find_element_by_visible_text(self, element_text):
        case_insensitive_element_x_path = \
            f"//*[text()[contains(translate(., '{element_text.upper()}', '{element_text.lower()}'), '{element_text.lower()}')]]"
        return self.find_element_by_x_path(case_insensitive_element_x_path)

    def find_element_within_iframe(self, iframe_title, element_x_path):
        iframe = self.find_element_by_x_path(
            f'//iframe[@title="{iframe_title}"]')
        self.driver.switch_to.frame(iframe)
        element = self.find_element_by_x_path(element_x_path)
        self.driver.switch_to.default_content
        return element

    def click_on_element(self, element):
        try:
            element.click()
            return True
        except:
            logging.warning("Unable to click on the element")
            return False

    def fill_in_input_field(self, input_field, text):
        try:
            for character in text:
                input_field.send_keys(character)
            return True
        except:
            logging.warning(
                f"Unable to fill in the input field: {input_field}")
            return False

    def quit(self):
        self.driver.quit()
