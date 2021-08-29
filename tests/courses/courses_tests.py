from pages.courses.courses_page import CoursesPage
from utilities.result_status import ResultStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courseP = CoursesPage(self.driver)
        self.rs = ResultStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidPurchase(self):
        result = self.courseP.doIt("test@email.com", "abcabc", "automation bundle", "1231456584562315", "1223", "123")
        assert result == True