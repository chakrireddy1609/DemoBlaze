from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import config_data


class HomePage:

    laptop_click_button = (By.XPATH,"//*[@id='itemc' and text()='Laptops']")
    laptop_select_button = (By.XPATH, "//*[@class='hrefch' and text()='MacBook Pro']")
    laptop_cost_text = (By.XPATH,"//*[@id='tbodyid'']/div[6]/div/div/h5")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(config_data.base_url)

    def laptop_click(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def laptop_cost(self,by_locator,expected_cost):
        actual_cost = WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(by_locator)).text
        assert actual_cost == expected_cost

    def laptop_select(self,by_locator):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(by_locator)).click()



