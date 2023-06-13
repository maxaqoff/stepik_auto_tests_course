from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_FORM).click()
        self.solve_quiz_and_get_code()

    #this func compare price between product price and basket price
    def compare_price(self):
        assert self.get_curr_product_price() == self.get_added_basket_price(), 'Price in basket != product price'

    #this func compare product name on product page and product name in basket after add product there
    def compare_product_name(self):
        assert self.get_curr_product_name() in self.get_added_product_names(), 'Value "product name" not in basket'

    #func for getting product price of basket
    def get_added_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_BASKET_PRICE).text

    # func for getting product name of products in basket
    def get_added_product_names(self):
        return [product.text for product in self.browser.find_elements(*ProductPageLocators.ADDED_PRODUCT_NAME)]

    # func for getting product name of product on product page
    def get_curr_product_name(self):
        return self.browser.find_element(*ProductPageLocators.CURR_PRODUCT_NAME).text

    # func for getting product price on product page
    def get_curr_product_price(self):
        return self.browser.find_element(*ProductPageLocators.CURR_PRODUCT_PRICE).text

    # func for check, that success message is desapear after adding product in basket
    def should_be_desapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should be desapear, but should not desapear"

    # func for check, that there is no success message on product page
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

