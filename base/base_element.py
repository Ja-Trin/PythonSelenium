from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.ui import WebDriverWait
from typing import List


class BaseElement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.5)

    def __get_element_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'xpath': By.XPATH,
                    'id': By.ID,
                    'name': By.NAME}
        return locating[find_by]

    def is_visible(self, find_by, locator: str, name: str = None) -> WebElement:
        return \
            self.wait.until(exp_cond.visibility_of_element_located((self.__get_element_by(find_by), locator)), name)

    def are_all_presents(self, find_by, locator: str, name: str = None) -> List[WebElement]:
        return \
            self.wait.until(exp_cond.presence_of_all_elements_located((self.__get_element_by(find_by), locator)), name)

    def is_clickable(self, find_by, locator: str, name: str = None) -> WebElement:
        return \
            self.wait.until(exp_cond.element_to_be_clickable((self.__get_element_by(find_by), locator)), name)

    def wait_staleness_of(self, web_element: WebElement):
        self.wait.until(exp_cond.staleness_of(web_element))
