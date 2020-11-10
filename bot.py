import time
import logging

from webdriver import WebDriver


class Bot:
    def __init__(self, start_page_url):
        self.webdriver = WebDriver()
        self.start_page_url = start_page_url
        logging.info("Initialized a bot instance")

    def go_to_start_page(self):
        self.webdriver.open_url(self.start_page_url)

    def refresh(self):
        self.webdriver.refresh()

    def quit(self):
        self.webdriver.quit()

    def is_on_start_page(self):
        return self.webdriver.get_current_url() == self.start_page_url

    def __fill_in_email(self, email):
        email_address_input_field = self.webdriver.find_element_by_name(
            'emailAddress')
        return self.webdriver.fill_in_input_field(email_address_input_field, email)

    def __fill_in_password(self, password):
        email_address_input_field = self.webdriver.find_element_by_name(
            'password')
        return self.webdriver.fill_in_input_field(email_address_input_field, password)

    def __click_on_member_checkout(self):
        member_checkout_button = self.webdriver.find_element_by_class(
            'checkoutLoginSubmit')
        return self.webdriver.click_on_element(member_checkout_button)

    def log_in(self, email, password):
        is_email_filled_in = self.__fill_in_email(email)
        is_password_filled_in = self.__fill_in_password(password)
        if is_email_filled_in and is_password_filled_in:
            return self.__click_on_member_checkout()
        return False

    def select_shoe(self, shoe_position):
        shoe_button = self.webdriver.find_element_by_x_path(
            f'//figure[{shoe_position}]')
        return self.webdriver.click_on_element(shoe_button)

    def select_shoe_size(self, size_position):
        size_button = self.webdriver.find_element_by_x_path(
            f'(//*[@class="size-grid-dropdown size-grid-button"])[{size_position}]')
        return self.webdriver.click_on_element(size_button)

    def add_to_cart(self):
        add_to_cart_button = self.webdriver.find_element_by_x_path(
            '//*[@data-qa="add-to-cart"]')
        return self.webdriver.click_on_element(add_to_cart_button)

    def go_to_checkout(self):
        checkout_button = self.webdriver.find_element_by_x_path(
            '//*[@data-qa="checkout-link"]')
        return self.webdriver.click_on_element(checkout_button)

    def wait_till_on_checkout_page(self):
        while not self.webdriver.get_current_url() == "https://www.nike.com/checkout":
            logging.info("not on checkout yet")
            time.sleep(0.5)
        time.sleep(2)
        return True

    def fill_in_cvv(self, cvv):
        cvv_input_field = self.webdriver.find_element_within_iframe(
            'Credit Card CVV Form', '//input[@id="cvNumber"]')
        return self.webdriver.fill_in_input_field(cvv_input_field, cvv)

    def continue_to_order_overview(self):
        continue_to_order_overview_button = self.webdriver.find_element_by_x_path('//*[@id="payment"]/div/div[1]/div[2]/div[5]/button')
        return self.webdriver.click_on_element(continue_to_order_overview_button)
