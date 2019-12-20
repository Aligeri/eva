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
        sql.add_currencies_by_email(user, "doge", "xem", "usdc_etht")
        sql.clear_show_after_removing_wallet_popup_by_email(user)
        return clear_added_wallets_fixture
    return clear_added_wallets

@pytest.fixture(scope='function')
def prepare_for_check_popup_checkbox():
    sql.add_currencies_by_email(UserforCheckPopupCheckbox.email, "doge", "xem")
    sql.clear_show_after_removing_wallet_popup_by_email(UserforCheckPopupCheckbox.email)
    yield



class TestClass:

    @xray("QA-1693")
    def test_add_wallets_currencies_availability(self, driver):
        loginPage = LoginPage(driver)
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
        loginPage.login_as_basic_user(UserforAddWalletFromFeatured.email, UserforCheckAddWallets.password)
        loginPage.input_pincode_login(UserforAddWalletFromFeatured.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.add_from_featured(Featured.FeaturedXEMClicable, MyWallets.XEM)

    @xray("QA-1696")
    def test_add_wallet_from_coins(self, driver, clear_added_wallets_fixture):
        clear_added_wallets_fixture(user=UserforAddWalletFromCoins.email)
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforAddWalletFromCoins.email, UserforAddWalletFromCoins.password)
        loginPage.input_pincode_login(UserforAddWalletFromCoins.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.add_from_coins(Coins.CoinsDOGEClicable, MyWallets.DOGE)

    @xray("QA-1697")
    def test_add_wallet_from_tokens(self, driver, clear_added_wallets_fixture):
        clear_added_wallets_fixture(user=UserforAddWalletFromTokens.email)
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforAddWalletFromTokens.email, UserforAddWalletFromTokens.password)
        loginPage.input_pincode_login(UserforAddWalletFromTokens.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.add_from_tokens(Tokens.TokensUSDCClicable, MyWallets.USDC)

    @xray("QA-1698", "QA-1700")
    def test_check_delete_popup(self, driver, prepare_for_delete_fixture):
        prepare_for_delete_fixture(user=UserforCheckDeletePopup.email)
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforCheckDeletePopup.email, UserforCheckDeletePopup.password)
        loginPage.input_pincode_login(UserforCheckDeletePopup.pincode)
        loginPage.wait_and_click_element_within_element(MyWallets.DOGE, MyWallets.IconTrash)
        loginPage.wait_until_element_visible(MyWallets.PupupDontShowAgain)
        loginPage.wait_and_click_element_within_element(MyWallets.PupupDontShowAgain, MyWallets.GotItButton)
        loginPage.wait_until_element_invisible(MyWallets.DOGE)

    @xray("QA-1699")
    @pytest.mark.usefixtures("prepare_for_check_popup_checkbox")
    def test_check_popup_checkbox(self, driver):
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforCheckPopupCheckbox.email, UserforCheckPopupCheckbox.password)
        loginPage.input_pincode_login(UserforCheckPopupCheckbox.pincode)
        loginPage.wait_and_click_element_within_element(MyWallets.DOGE, MyWallets.IconTrash)
        loginPage.wait_until_element_visible(MyWallets.PupupDontShowAgain)
        loginPage.wait_and_click_element_within_element(MyWallets.PupupDontShowAgain, MyWallets.CheckBox)
        loginPage.wait_and_click_element_within_element(MyWallets.PupupDontShowAgain, MyWallets.GotItButton)
        loginPage.wait_and_click_element_within_element(MyWallets.XEM, MyWallets.IconTrash)
        loginPage.wait_until_element_invisible(MyWallets.PupupDontShowAgain,1)
        loginPage.wait_until_element_invisible(MyWallets.XEM)

    @xray("QA-1742")
    def test_check_delete_from_tokens(self, driver, prepare_for_delete_fixture):
        prepare_for_delete_fixture(user=UserforDeleteFromTokens.email)
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforDeleteFromTokens.email, UserforDeleteFromTokens.password)
        loginPage.input_pincode_login(UserforDeleteFromTokens.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.delete_from_tokens(Tokens.TokensUSDCClicable, MyWallets.USDC)

    @xray("QA-1743")
    def test_check_delete_from_coins(self, driver, prepare_for_delete_fixture):
        prepare_for_delete_fixture(user=UserforDeleteFromCoins.email)
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforDeleteFromCoins.email, UserforDeleteFromCoins.password)
        loginPage.input_pincode_login(UserforDeleteFromCoins.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.delete_from_coins(Coins.CoinsDOGEClicable, MyWallets.DOGE)

    @xray("QA-1744")
    def test_check_delete_from_featured(self, driver, prepare_for_delete_fixture):
        prepare_for_delete_fixture(user=UserforDeleteFromFeatured.email)
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforDeleteFromFeatured.email, UserforDeleteFromFeatured.password)
        loginPage.input_pincode_login(UserforDeleteFromFeatured.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.delete_from_featured(Featured.FeaturedXEMClicable, MyWallets.XEM)

    @xray("QA-1706")
    def test_search(self, driver, clear_added_wallets_fixture):
        clear_added_wallets_fixture(user=UserforTestSearchAddWallets.email)
        loginPage = LoginPage(driver)
        loginPage.login_as_basic_user(UserforTestSearchAddWallets.email, UserforTestSearchAddWallets.password)
        loginPage.input_pincode_login(UserforTestSearchAddWallets.pincode)
        addWalletsPage = AddWalletsPage(driver)
        addWalletsPage.test_search_input()