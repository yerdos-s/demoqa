from selenium.webdriver.common.by import By


class AutomationPracticeFormLocators:
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    EMAIL = (By.ID, 'userEmail')
    GENDER_MALE = (By.ID, 'gender-radio-1')
    GENDER_FEMALE = (By.ID, 'gender-radio-2')
    GENDER_OTHER = (By.ID, 'gender-radio-3')
    DOB = (By.ID, 'dateOfBirthInput')
    SUBJECTS = (By.ID, 'subjectsContainer')
    HOBBIES_SPORTS = (By.ID, 'hobbies-checkbox-1')
    HOBBIES_READING = (By.ID, 'hobbies-checkbox-2')
    HOBBIES_MUSIC = (By.ID, 'hobbies-checkbox-3')
    PICTURE_FILE = (By.ID, 'uploadPicture')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    STATE = (By.ID, 'state')
    CITY = (By.ID, 'city')
