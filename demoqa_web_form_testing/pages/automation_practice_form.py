from .basepage import BasePage
from .locators import AutomationPracticeFormLocators
from selenium.webdriver.common.keys import Keys


class AutomationPracticeFormPage(BasePage):

    def should_be_automation_practice_form_in_url(self):
        assert 'automation-practice-form' in self.url, 'There is no automation-practice-form in url'

    def should_be_first_name_field_present(self):
        self.is_element_present(*AutomationPracticeFormLocators.FIRST_NAME)
        assert True, 'First name field is not presented'

    def should_be_last_name_field_present(self):
        self.is_element_present(*AutomationPracticeFormLocators.LAST_NAME)
        assert True, 'First name field is not presented'

    def should_be_email_field_present(self):
        self.is_element_present(*AutomationPracticeFormLocators.EMAIL)
        assert True, 'Email field is not presented'

    def should_be_gender_male_radiobutton_present(self):
        self.is_element_present(*AutomationPracticeFormLocators.GENDER_MALE)
        assert True, 'Male gender radiobutton is not presented'

    def should_be_date_of_birth_field_present(self):
        self.is_element_present(*AutomationPracticeFormLocators.DOB)
        assert True, 'Date of birth datepicker is not presented'

    def add_value_to_first_name(self, value):
        self.browser.find_element(*AutomationPracticeFormLocators.FIRST_NAME).clear()
        self.browser.find_element(*AutomationPracticeFormLocators.FIRST_NAME).send_keys(
            value)

    def should_display_first_name_value(self, value):
        input_value = self.browser.find_element(*AutomationPracticeFormLocators.FIRST_NAME).get_attribute('value')
        assert input_value == value

    def add_value_to_last_name(self, value):
        self.browser.find_element(*AutomationPracticeFormLocators.LAST_NAME).clear()
        self.browser.find_element(*AutomationPracticeFormLocators.LAST_NAME).send_keys(
            value)

    def should_display_last_name_value(self, value):
        input_value = self.browser.find_element(*AutomationPracticeFormLocators.LAST_NAME).get_attribute('value')
        assert input_value == value

    def select_gender_male_radiobutton(self):
        element = self.browser.find_element(*AutomationPracticeFormLocators.GENDER_MALE)
        self.browser.execute_script("arguments[0].click();", element)

    def should_be_gender_male_radiobutton_selected(self):
        assert self.is_element_present(*AutomationPracticeFormLocators.GENDER_MALE) == True

    def add_value_to_email(self, value):
        self.browser.find_element(*AutomationPracticeFormLocators.EMAIL).clear()
        self.browser.find_element(*AutomationPracticeFormLocators.EMAIL).send_keys(
            value)

    def should_display_email_value(self, value):
        input_value = self.browser.find_element(*AutomationPracticeFormLocators.EMAIL).get_attribute('value')
        assert input_value == value

    def should_be_picture_uploader_present(self):
        self.is_element_present(*AutomationPracticeFormLocators.PICTURE_FILE)
        assert True, 'Picture file (Uploader) is not presented'

    def upload_picture(self, picture):
        file_input = self.browser.find_element(*AutomationPracticeFormLocators.PICTURE_FILE)
        file_input.send_keys(picture)
