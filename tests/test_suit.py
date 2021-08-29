import unittest
from tests.home.login_tests import LoginTest
from tests.courses.courses_tests import CourseTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CourseTest)

smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)