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

    def delete_coin(self, delete_locator, my_wallets_locator):
        """
        удаляет валюту
        :param delete_locator: локатор иконки валюты в add wallets
        :param my_wallets_locator: локатор в my wallets, где должны увидеть что валюта убралась
        :return:
        """
        self.wait_and_click(delete_locator)
        self.wait_until_element_visible(MyWallets.PupupDontShowAgain)
        self.wait_and_click_element_within_element(MyWallets.PupupDontShowAgain, MyWallets.GotItButton)
        self.wait_until_element_invisible(my_wallets_locator, 1)

    def delete_from_tokens(self, delete_locator, my_wallets_locator):
        """
        удаляет валюту со вкладки Tokens
        :param delete_locator: локатор иконки валюты во вкладке tokens, с которого снимаем галочку
        :param my_wallets_locator: локатор в my wallets, где должны увидеть что валюта убралась
        :return:
        """
        self.wait_and_click(AddWalletsElements.AddWalletsButton)
        self.navigate_to_tokens()
        self.delete_coin(delete_locator, my_wallets_locator)

    def delete_from_coins(self, delete_locator, my_wallets_locator):
        """
        удаляет валюту со вкладки Coins
        :param delete_locator: локатор иконки валюты во вкладке coins, с которого снимаем галочку
        :param my_wallets_locator: локатор в my wallets, где должны увидеть что валюта убралась
        :return:
        """
        self.wait_and_click(AddWalletsElements.AddWalletsButton)
        self.navigate_to_coins()
        self.delete_coin(delete_locator, my_wallets_locator)

    def delete_from_featured(self, delete_locator, my_wallets_locator):
        """
        удаляет валюту со вкладки Featured
        :param delete_locator: локатор иконки валюты во вкладке featured, с которого снимаем галочку
        :param my_wallets_locator: локатор в my wallets, где должны увидеть что валюта убралась
        :return:
        """
        self.wait_and_click(AddWalletsElements.AddWalletsButton)
        self.delete_coin(delete_locator, my_wallets_locator)

    def test_search_input(self):
        """
        проверка добавления нескольких валют чарез поиск
        """
        self.wait_and_click(AddWalletsElements.AddWalletsButton)
        self.wait_until_element_visible(AddWalletsElements.SearchInput)
        self.wait_and_input_text(AddWalletsElements.SearchInput, "do")
        self.wait_and_click(Coins.CoinsDOGEClicable)
        self.clear_field(AddWalletsElements.SearchInput)
        self.wait_and_input_text(AddWalletsElements.SearchInput, "xe")
        self.wait_and_click(Coins.CoinsXEMClicable)
        self.clear_field(AddWalletsElements.SearchInput)
        self.wait_and_input_text(AddWalletsElements.SearchInput, "us")
        self.wait_and_click(Tokens.TokensUSDCClicable)
        self.wait_until_element_visible(MyWallets.DOGE)
        self.wait_until_element_visible(MyWallets.XEM)
        self.wait_until_element_visible(MyWallets.USDC)