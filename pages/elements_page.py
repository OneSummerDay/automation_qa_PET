from selenium.webdriver import Keys

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Artem')
        self.element_is_visible(self.locators.EMAIL).send_keys('artem@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Zp')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Tokmak')
        self.element_is_visible(self.locators.SUBMIT).send_keys(Keys.ENTER)

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address




