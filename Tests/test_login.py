from Config.config import config_data
from Pages.LoginPage import LoginPage
from Tests.BaseTest import Test_Base


class Test_Login(Test_Base):

    def test_login(self):

        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_login(LoginPage.login_button)
        self.loginpage.input_username(LoginPage.username_text,config_data.username)
        self.loginpage.input_password(LoginPage.password_text,config_data.password)
        self.loginpage.click_submit(LoginPage.submit_button)

    def test_title(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.verify_title(config_data.homepage_title)

