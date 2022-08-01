from base.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BaseElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.HOMEPAGE_CARDS: str = "//img[starts-with(@class, 'home_page')]"
        self.SEARCH_TEXTBOX: str = "//input[@name='term' and @type='text']"
        self.SEARCH_BTN: str = "//a[@id='store_search_link']//img[@src]"

    def __get_home_cards(self) -> WebElement:
        return self.is_clickable('xpath', self.HOMEPAGE_CARDS, 'Home Cards')

    def __get_search_textbox(self) -> WebElement:
        return self.is_clickable('xpath', self.SEARCH_TEXTBOX, 'Search Field')

    def __get_search_btn(self) -> WebElement:
        return self.is_clickable('xpath', self.SEARCH_BTN, 'Search Button')

    def is_home_page_present(self) -> bool:
        return self.__get_home_cards()

    def send_text_to_search_textbox(self, game_name: str):
        search_textbox = self.__get_search_textbox()
        search_textbox.send_keys(game_name)

    def click_search_btn(self):
        search_btn = self.__get_search_btn()
        search_btn.click()
