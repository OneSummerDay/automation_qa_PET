import time

from pages.base_page import BasePage

#Test
def test(driver):
    page = BasePage(driver, 'https://www.google.com')
    page.open()
    time.sleep(3)
