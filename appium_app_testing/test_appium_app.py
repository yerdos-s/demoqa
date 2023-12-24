import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'app': r'C:\Users\sadvakasov\appiumSandbox\app_used\goshady.words.prod_9.95.0-API24apkmirror.com.apk',
    'appPackage': 'goshady.words.prod',
    'appWaitActivity': 'goshady.words.ui.main.MainActivity'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


class TestApplication:
    @pytest.mark.order(1)
    @pytest.mark.parametrize("username, password, expected_result", [
        ("Yerdos_valid_user", "valid_password123", "Login successful"),
        ("invalid_user", "valid_password123", "Invalid username"),
        ("Yerdos_valid_user", "invalid_pass", "Invalid password"),
        ("invalid_user", "invalid_pass", "You submitted wrong username or password. Please try again."),
        ("", "", "Please enter username or password"),
    ])
    def test_login(username, password, expected_result):
        username_field = driver.find_element(MobileBy.ID, "username_input")
        username_field.send_keys(username)
        password_field = driver.find_element(MobileBy.ID, "password_input")
        password_field.send_keys(password)
        login_button = driver.find_element(MobileBy.ID, "login_button")
        login_button.click()
        result_message = driver.find_element(MobileBy.ID, "result_window")
        assert result_message.text == expected_result

    @pytest.mark.order(2)
    def test_add_product_to_cart_from_main_view(self):
        product = driver.find_element(MobileBy.ID, 'product-item-1')
        product.click()
        add_to_cart_button = driver.find_element(MobileBy.ID, 'add_to_cart_button')
        add_to_cart_button.click()
        cart_view = driver.find_element(MobileBy.ID, 'tapbar_cart')
        cart_view.click()
        item_in_cart = driver.find_element(MobileBy.ID, 'item-1')
        assert product.text in item_in_cart.text

    @pytest.mark.order(3)
    def test_increase_product_amount_in_cart_view(self):
        cart_view = driver.find_element(MobileBy.ID, 'tapbar_cart')
        cart_view.click()
        increase_amount_button = driver.find_element(MobileBy.ID,'increase_amount_button')
        increase_amount_button.click()
        product_amount = driver.find_element(MobileBy.ID,'item_overall_number')
        assert product_amount.text == "2", "The amount of products is not 2"

    @pytest.mark.order(4)
    def test_decrease_product_amount_in_cart_view(self):
        cart_view = driver.find_element(MobileBy.ID, 'tapbar_cart')
        cart_view.click()
        increase_amount_button = driver.find_element(MobileBy.ID,'decrease_amount_button')
        increase_amount_button.click()
        product_amount = driver.find_element(MobileBy.ID,'item_overall_number')
        assert product_amount.text == "1", "The amount of products is not 1"

    @pytest.mark.order(5)
    def test_remove_product_from_cart_view(self):
        cart_view = driver.find_element(MobileBy.ID, 'tapbar_cart')
        cart_view.click()
        item_in_cart = driver.find_element(MobileBy.ID, 'item-1')
        remove_from_basket_button = driver.find_element(MobileBy.ID, 'delete_item_button')
        remove_from_basket_button.click()
        assert not item_in_cart, "Item is present, but it should be removed"
