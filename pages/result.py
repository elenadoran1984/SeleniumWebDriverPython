"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoResultPage:
    #Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    #Initializer
    def __init__(self, browser):
        self.browser = browser

    #Interaction Methods

    # def result_link_titles(self):
    #     links = self.browser.find_elements(*self.RESULT_LINKS)
    #     titles = [link.text for link in links]
    #     return titles

    # def result_link_titles(self):
    #     links = self.browser.find_elements(*self.RESULT_LINKS)
    #     titles = []
    #     for link in links:
    #         title = link.text
    #         titles.append(title)
    #         print("Found title:", title)
    #     return titles

    def result_link_titles(self):

        # Wait until at least one search result link is present
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.RESULT_LINKS)
        )
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = []
        for link in links:
            title = link.text
            titles.append(title)
            print("Found title:", title)
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title
