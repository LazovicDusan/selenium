from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class CoursesPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "//input[@placeholder='Email Address']"
    _password_field = "//input[@placeholder='Password']"
    _login_button = "//input[@value='Login']"
    _all_courses = "//a[text()='ALL COURSES']"
    _search = "//input[@name='course']"
    _search_button = "//button[@class='find-course search-course']"
    _course = "//img[@alt='course image']"
        # "//div[@class='zen-course-list']"
    _enroll_button = "//button[text()='Enroll in Bundle']"
    _exp_date = "//input[@name='exp-date']"
    _cvc = "//input[@name='cvc']"
    _card_no = "//input[@placeholder='Card Number']"
    _buy_button = "//button[text()='Buy']"
    _invalid_info = "//span[text()='Your card number is invalid.']"

    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def clickAllCourses(self):
        self.elementClick(self._all_courses)

    def searchCourses(self, data):
        self.sendKeys(data, self._search)

    def clickSearchButton(self):
        self.elementClick(self._search_button)

    def clickCourse(self):
        self.elementClick(self._course)

    def clickToEnroll(self):
        self.elementClick(self._enroll_button)

    def enterCardNo(self, cardNo):
        self.switchToFrame(id=1)
        self.sendKeys(cardNo, self._card_no)
        self.switchToDefaultContent()

    def enterExpDate(self, expDate):
        self.switchToFrame(id=2)
        self.sendKeys(expDate, self._exp_date)
        self.switchToDefaultContent()

    def enterCvc(self, cvc):
        self.switchToFrame(id=3)
        self.sendKeys(cvc, self._cvc)
        self.switchToDefaultContent()

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def searchCourseForPurchase(self, name=""):
        self.clickAllCourses()
        self.searchCourses(name)
        time.sleep(2)
        self.clickSearchButton()
        time.sleep(2)
        self.clickCourse()

    def enrollSelectedCourse(self):
        self.clickToEnroll()

    def enterPaymentInfo(self, cardNo="", expDate="", cvc=""):
        self.scrollPage()
        self.enterCardNo(cardNo)
        time.sleep(10)
        self.enterExpDate(expDate)
        time.sleep(10)
        self.enterCvc(cvc)

    def validateInvalidEntry(self):
        result = self.isElementPresent(self._invalid_info)
        return result

    def doIt(self, email, password, name, cardNo, expDate, cvc):
        self.login(email, password)
        time.sleep(2)
        self.searchCourseForPurchase(name)
        time.sleep(2)
        self.enrollSelectedCourse()
        time.sleep(2)
        self.enterPaymentInfo(cardNo, expDate, cvc)
        time.sleep(2)
        return self.validateInvalidEntry()

