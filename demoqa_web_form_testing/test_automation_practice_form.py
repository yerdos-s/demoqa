from pages.automation_practice_form import AutomationPracticeFormPage
import pytest
import os
import time


@pytest.fixture()
def link():
    yield 'https://demoqa.com/automation-practice-form'


@pytest.fixture()
def picture_path():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    picture_path = os.path.join(current_dir, "cat.jpg")
    yield picture_path


@pytest.mark.parametrize("first_name", ["Yerdos", "Test123!@#$%^&*()_+=/", " "])
def test_user_can_add_value_in_first_name_field(browser, first_name, link):
    page = AutomationPracticeFormPage(browser, link)
    page.open()
    page.should_be_first_name_field_present()
    page.add_value_to_first_name(first_name)
    page.should_display_first_name_value(first_name)


@pytest.mark.parametrize("last_name", ["Sadvakasov", "Test123!@#$%^&*()_+=/", " "])
def test_user_can_add_value_in_last_name_field(browser, last_name, link):
    page = AutomationPracticeFormPage(browser, link)
    page.open()
    page.should_be_last_name_field_present()
    page.add_value_to_last_name(last_name)
    page.should_display_last_name_value(last_name)


def test_user_can_select_gender_male_radiobutton(browser, link):
    page = AutomationPracticeFormPage(browser, link)
    page.open()
    page.should_be_gender_male_radiobutton_present()
    page.select_gender_male_radiobutton()
    page.should_be_gender_male_radiobutton_selected()


@pytest.mark.parametrize("email", ["admin@admindata.com", "Test123!@#$%^&*()_+=/", " "])
def test_user_can_add_email(browser, email, link):
    page = AutomationPracticeFormPage(browser, link)
    page.open()
    page.should_be_email_field_present()
    page.add_value_to_email(email)
    page.should_display_email_value(email)


def test_user_can_upload_picture(browser, picture_path, link):
    page = AutomationPracticeFormPage(browser, link)
    page.open()
    page.should_be_picture_uploader_present()
    page.upload_picture(picture_path)
