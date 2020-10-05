from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import config_data


class LoginPage:

    login_button = (By.ID,'login2')
    username_text = (By.ID,'loginusername')
    password_text = (By.ID,'loginpassword')
    submit_button = (By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')

    def __init__(self,driver):
        self.driver = driver
        self.driver.get(config_data.base_url)

    def click_login(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def input_username(self,by_locator,username):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(username)

    def input_password(self,by_locator,password):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(password)

    def click_submit(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def verify_title(self,expected_title):
        assert self.driver.title == expected_title






