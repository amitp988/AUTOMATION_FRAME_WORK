from selenium import webdriver
from Pages.Home.Login_Page import Loginpage
import unittest

class LoginTest(unittest.TestCase):

    def login_test(self):
        Base_Url = "https://letskodeit.teachable.com/"
        Path = "D:\\SELENIUM DRIVERS\\CHROME\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=Path)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(Base_Url)

        lp = Loginpage(driver)
        lp.login_page("amitpatnaik988@gmail.com", "Amiy@1234")




