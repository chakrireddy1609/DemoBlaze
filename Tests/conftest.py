import pytest
from selenium import webdriver

from Config.config import config_data


@pytest.fixture(params=["chrome"],scope="class")
def init_driver(request):

    web_driver = webdriver.Chrome(executable_path=config_data.executable_path)
    request.cls.driver = web_driver
    yield
    web_driver.close()

def pytest_configure(config):
    config._metadata['Project Name'] = "Nop Commerce"
    config._metadata['Module Name'] = "E2E"
    config._metadata['QA Responsible'] = "Chakri"


