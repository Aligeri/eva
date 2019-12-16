from Pages.BasePage import *
from Locators.AddWalletsLocators import *
import time

class AddWalletsPage(Page):

    def navigate_to_coins(self):
        self.wait_and_click(AddWalletsElements.CoinsTab)

    def navigate_to_tokens(self):
        self.wait_and_click(AddWalletsElements.TokensTab)

    def add_from_featured(self, add_locator, my_wallets_locator):
        """
        добавляет валюту со вкладки Featured
        :param add_locator: локатор, куда кликаем для добавления
        :param my_wallets_locator: локатор в my wallets, где должны увидеть что оно добавилось
        :return:
        """
        self.wait_and_click(AddWalletsElements.AddWalletsButton)
        self.wait_and_click(add_locator)
        self.wait_and_click(my_wallets_locator)

    def add_from_coins(self, add_locator, my_wallets_locator):
        """
        добавляет валюту со вкладки Coins
        :param add_locator: локатор, куда кликаем для добавления
        :param my_wallets_locator: локатор в my wallets, где должны увидеть что оно добавилось
        :return:
        """
        self.wait_and_click(AddWalletsElements.AddWalletsButton)
        self.navigate_to_coins()
        self.wait_and_click(add_locator)
        self.wait_and_click(my_wallets_locator)

    def add_from_tokens(self, add_locator, my_wallets_locator):
        """
        добавляет валюту со вкладки Tokens
        :param add_locator: локатор, куда кликаем для добавления
        :param my_wallets_locator: локатор в my wallets, где должны увидеть что оно добавилось
        :return:
        """
        self.wait_and_click(AddWalletsElements.AddWalletsButton)
        self.navigate_to_tokens()
        self.wait_and_click(add_locator)
        self.wait_and_click(my_wallets_locator)