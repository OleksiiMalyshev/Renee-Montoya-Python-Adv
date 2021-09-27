import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('First', 'Last', 100)

    def test_info_about_employeer(self):
        self.assertEqual(self.employee.first, 'First')
        self.assertEqual(self.employee.last, 'Last')
        self.assertEqual(self.employee.pay, 100)

    def test_email(self):
        self.assertEqual(self.employee.email, 'First.Last@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname,'First Last')

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, 105)

    @patch('requests.get')
    def test_monthly_schedule(self, mocker):
        class MyMocker():
            ok = True
            text = 'First Last'

        mocker.return_value = MyMocker()
        self.assertEqual(self.employee.monthly_schedule(1), 'First Last')
