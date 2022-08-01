import pytest
from pom.homepage import HomePage
from pom.searchpage import SearchPage
from utils import json_util as ju


@pytest.mark.usefixtures('setup')
class TestSteam:

    def test_sort_games(self):
        td = ju.JsonUtil.read_json_from_resources(rf'resources\test_data.json')
        game_name = td['game_name']
        top_n = td['top_n']
        needed_attribute = td['needed_attribute']

        home_page = HomePage(self.driver)
        assert home_page.is_home_page_present()
        home_page.send_text_to_search_textbox(game_name)
        home_page.click_search_btn()

        search_page = SearchPage(self.driver)
        assert search_page.is_search_page_present()
        assert search_page.is_games_list_not_empty()
        search_page.click_sort_by_trigger()
        search_page.click_sort_by_desc_btn()
        assert search_page.are_prices_sorting_right(top_n, needed_attribute)
