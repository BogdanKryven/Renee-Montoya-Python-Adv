from employee import Employee
from unittest.mock import patch
from unittest import TestCase
import pytest


class TestAttributes:

    def test_employee_fixture_email(self, employee_email):
        assert employee_email == "Bohdan.Kryven@email.com"

    @pytest.mark.parametrize("name, surname, expected_result",
                             [("Bohdan", "Kryven", "Bohdan.Kryven@email.com"),
                              ("Andriy", "Lunin", "Andriy.Lunin@email.com"),
                              ("Taras", "Bilas", "Taras.Bilas@email.com"),
                              ("Ruslan", "Piton", "Ruslan.Piton@email.com"),
                              ("Natalia", "Strohush", "Natalia.Strohush@email.com"),
                              ("Yaryna", "Voitenko", "Yaryna.Voitenko@email.com"),
                              ("Anastasia", "Poplavska", "Anastasia.Poplavska@email.com")])
    def test_employee_email(self, name, surname, expected_result):
        assert Employee(name, surname, 100).email == expected_result

    def test_employee_fixture_fullname(self, employee_fullname):
        assert employee_fullname == "Bohdan Kryven"

    def test_employee_fixture_raise(self, employee_raise):
        assert employee_raise() == 105

    def test_employee_fixture_fullname_and_email(self, employee_fullname_and_email):
        assert employee_fullname_and_email() == "Bohdan Kryven \nBohdan.Kryven@email.com"


class TestResponse(TestCase):

    def setUp(self) -> None:
        self.employee = Employee("Bohdan", "Kryven", 100)

    @patch('employee.requests.get')
    def test_response(self, mocker):
        mocker.return_value.ok = True
        mocker.return_value.text = "Some test text"
        result = self.employee.monthly_schedule('september')
        self.assertIsNotNone(result)
        self.assertNotEqual(result, 'Some test text1')
        self.assertEqual(result, "Some test text")
