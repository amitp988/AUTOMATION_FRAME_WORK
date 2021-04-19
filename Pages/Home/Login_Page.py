from selenium import webdriver
from selenium.webdriver.common.by import By

class Loginpage():

    def __init__(self, driver):
        self.driver = driver

    def login_page(self, username, password):

        login_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        login_link.click()

        user_name = self.driver.find_element(By.ID, "user_email")
        user_name.send_keys(username)

        pass_word = self.driver.find_element(By.ID, "user_password")
        pass_word.send_keys(password)

        login_button = self.driver.find_element(By.NAME, "commit")
        login_button.click()
