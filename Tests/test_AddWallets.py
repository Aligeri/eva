import pytest
from Pages.LoginPage import *
from Pages.TransactionsPage import *
from Pages.BasePage import *
from Pages.AddWalletsPage import *
from Config.Users import *
from Helpers.SQLHelper import *
from Config.Users import *
from Locators.AddWalletsLocators import *
from xrayplugin.plugin import xray

sql = SQLHelper()

@pytest.fixture(scope='function')
def clear_added_wallets_fixture():
    def clear_added_wallets(user):
        sql.clear_added_currencies_by_email(user)
        return clear_added_wallets_fixture
    return clear_added_wallets

@pytest.fixture(scope='function')
def prepare_for_delete_fixture():
    def clear_added_wallets(user):
        sql.add_currency_by_email(user, "doge")
        return clear_added_wallets_fixture
    return clear_added_wallets


class TestClass:

    @xray("QA-1693")
    def test_add_wallets_currencies_availability(self, driver):
        loginPage = LoginPage(driver)
        loginPage.reset_session()
        loginPage.login_as_basic_user(UserforCheckAddWallets.email, UserforCheckAddWallets.password)
        loginPage.input_pincode_login(UserforCheckAddWallets.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.wait_and_click(AddWalletsElements.AddWalletsButton)
        addWalletsPage.wait_until_element_visible(Featured.FeaturedCardClickable)
        addWalletsPage.navigate_to_coins()
        addWalletsPage.wait_until_element_visible(Coins.CoinCircle)
        addWalletsPage.navigate_to_tokens()
        addWalletsPage.wait_until_element_visible(Tokens.TokenCircle)

    @xray("QA-1695")
    def test_add_wallet_from_featured(self, driver, clear_added_wallets_fixture):
        clear_added_wallets_fixture(user=UserforAddWalletFromFeatured.email)
        loginPage = LoginPage(driver)
        loginPage.reset_session()
        loginPage.login_as_basic_user(UserforAddWalletFromFeatured.email, UserforCheckAddWallets.password)
        loginPage.input_pincode_login(UserforAddWalletFromFeatured.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.add_from_featured(Featured.FeaturedXEMClicable, MyWallets.XEM)

    @xray("QA-1696")
    def test_add_wallet_from_featured(self, driver, clear_added_wallets_fixture):
        clear_added_wallets_fixture(user=UserforAddWalletFromCoins.email)
        loginPage = LoginPage(driver)
        loginPage.reset_session()
        loginPage.login_as_basic_user(UserforAddWalletFromCoins.email, UserforAddWalletFromCoins.password)
        loginPage.input_pincode_login(UserforAddWalletFromCoins.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.add_from_coins(Coins.CoinsDOGEClicable, MyWallets.DOGE)

    @xray("QA-1697")
    def test_add_wallet_from_featured(self, driver, clear_added_wallets_fixture):
        clear_added_wallets_fixture(user=UserforAddWalletFromTokens.email)
        loginPage = LoginPage(driver)
        loginPage.reset_session()
        loginPage.login_as_basic_user(UserforAddWalletFromTokens.email, UserforAddWalletFromTokens.password)
        loginPage.input_pincode_login(UserforAddWalletFromTokens.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.add_from_tokens(Tokens.TokensUSDCClicable, MyWallets.USDC)

    @xray("QA-1698")
    def test_check_delete_popup(self, driver, prepare_for_delete_fixture):
        prepare_for_delete_fixture(user=UserforCheckDeletePopup.email)
        loginPage = LoginPage(driver)
        loginPage.reset_session()
        loginPage.login_as_basic_user(UserforCheckDeletePopup.email, UserforCheckDeletePopup.password)
        loginPage.input_pincode_login(UserforCheckDeletePopup.pincode)