from base.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SearchPage(BaseElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.SEARCH_OPTIONS: str = "additional_search_options"
        self.SORT_BY: str = "sort_by_trigger"
        self.SORT_PRICE_DESC: str = "Price_DESC"
        self.PRICES: str = "//div[@class='col search_price_discount_combined responsive_secondrow']"
        self.GAMES_IN_RESULT: str = "//a[starts-with(@data-ds-itemkey,'App_')]"
        self.SEARCH_RESULT: str = "search_result_container"

    def __get_search_options(self) -> WebElement:
        return self.is_clickable('id', self.SEARCH_OPTIONS, 'Search Options')

    def __get_sort_by_trigger(self) -> WebElement:
        return self.is_clickable('id', self.SORT_BY, 'Sort-by Trigger')

    def __get_sort_by_desc_btn(self) -> WebElement:
        return self.is_clickable('id', self.SORT_PRICE_DESC, 'Sort by Desc')

    def __get_prices(self) -> List[WebElement]:
        return self.are_all_presents('xpath', self.PRICES, 'Price')

    def __get_games_in_result(self) -> List[WebElement]:
        return self.are_all_presents('xpath', self.GAMES_IN_RESULT, 'Games in Result')

    def __get_search_result(self) -> WebElement:
        return self.is_visible('id', self.SEARCH_RESULT, 'Search Result')

    def is_search_page_present(self) -> bool:
        return self.__get_search_options()

    def click_sort_by_trigger(self):
        sort_by_trigger = self.__get_sort_by_trigger()
        sort_by_trigger.click()

    def click_sort_by_desc_btn(self):
        sort_by_desc_btn = self.__get_sort_by_desc_btn()
        sort_by_desc_btn.click()

    def is_games_list_not_empty(self) -> bool:
        games_list = self.__get_games_in_result()
        return len(games_list) > 0

    def __get_final_prices(self, top_n: int, needed_attribute: str) -> List[int]:
        search_result = self.__get_search_result()
        self.wait_staleness_of(search_result)
        prices = self.__get_prices()
        final_prices = []
        for price in prices[0:top_n]:
            final_prices.append(int(int(price.get_attribute(needed_attribute)) / 100))
        return final_prices

    def are_prices_sorting_right(self, top_n: int, needed_attribute: str) -> bool:
        final_prices = self.__get_final_prices(top_n, needed_attribute)
        for currentPrice, nextPrice in zip(final_prices, final_prices[1:]):
            if currentPrice < nextPrice:
                return False
        return True
