from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Cassandra goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request, and does not load
        # the list page
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector(
                "#id_text:valid"
            )
        )

        # She starts typing some text and the error disappears
        self.get_item_input_box().send_keys("Buy milk")
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector(
                "#id_text:valid"
            )
        )

        # And she can submit is successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector(
                "#id_text:valid"
            )
        )

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys("Make tea")
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector(
                "#id_text:valid"
            )
        )
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for_row_in_list_table("2: Make tea")
