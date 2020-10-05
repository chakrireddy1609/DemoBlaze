from Config.config import config_data
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import Test_Base



class Test_home(Test_Base):


    def test_laptop(self):

        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_login(LoginPage.login_button)
        self.loginpage.input_username(LoginPage.username_text, config_data.username)
        self.loginpage.input_password(LoginPage.password_text, config_data.password)
        self.loginpage.click_submit(LoginPage.submit_button)
        self.homepage = HomePage(self.driver)
        self.homepage.laptop_click(HomePage.laptop_click_button)
        self.homepage.laptop_select(HomePage.laptop_select_button)





