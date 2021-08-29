from pages.home.login_page import LoginPage
from utilities.result_status import ResultStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.rs = ResultStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginSuccessful()
        self.rs.mark(result1, "Login logo is not present!")
        result2 = self.lp.verifyTitle("My Courses")
        self.rs.markFinal("test_validLogin", result2, "Title is incorrect!")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abc")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=4)
    def test_checkHomePageTitle(self):
        self.lp.logout()
        result = self.lp.verifyTitle("Home Page")
        assert result == True

    @pytest.mark.run(order=3)
    def test_checkLogedInTitle(self):
        result = self.lp.verifyTitle("My Courses")
        assert result == True

    @pytest.mark.run(order=5)
    def test_buyCourseInvalid(self):
        self.lp.login("test@email.com", "abcabc")

