from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "//input[@placeholder='Email Address']"
    _password_field = "//input[@placeholder='Password']"
    _login_button = "//input[@value='Login']"
    _logo = "//button[@id='dropdownMenu1']"
    _logout_button = "//a[text()='Logout']"
    _login_fail_lable = "//span[text()='Your username or password is invalid. Please try again.']"

    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def clickLogo(self):
        self.elementClick(self._logo)

    def clickLogoutButton(self):
        self.elementClick(self._logout_button)

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def logout(self):
        self.clickLogo()
        self.clickLogoutButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._logo)
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._login_fail_lable)
        return result

    def verifyTitle(self, title):
        if self.getTitle() == title:
            return True
        else:
            return False

    def clearFields(self):
        emailField = self.getElement(self._email_field)
        emailField.clear()
        passwordField = self.getElement(self._password_field)
        passwordField.clear()

