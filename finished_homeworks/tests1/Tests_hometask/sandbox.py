# import unittest
# from unittest.mock import patch
# from employee import Employee
#
#
# class TestEmployee(unittest.TestCase):
#
#     def setUp(self):
#         self.employee = Employee('First', 'Last', 100)
#
#     @patch('requests.get')
#     def test_monthly_schedule(self, mocker):
#         class MyMocker:
#             ok = True
#             text = 'First Last'
#
#         mocker.return_value = MyMocker()
#         self.assertEqual(self.employee.monthly_schedule("something wrong"), 'First Last')


# ======================================================================================================================


# import unittest
# from employee import Employee
# from unittest.mock import patch
#
#
# class mockResponseTrue:
#     status_code = 200
#     elapsed = 100
#     text = "True"
#     ok = True
#
#     def __init__(self, *args, **kwargs):
#         pass
#
#
# class mockResponseFalse:
#     status_code = 404
#     elapsed = 100
#     text = "False"
#     ok = False
#
#     def __init__(self, *args, **kwargs):
#         pass
#
#
# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         self.employeeTest = Employee('Jon', 'Sina', 120)
#
#     @patch("employee.requests.get")
#     def test_monthly_schedule(self, mocker):
#         mocker.side_effect = mockResponseTrue
#         self.assertEqual(self.employeeTest.monthly_schedule('september'), "True")
#         mocker.side_effect = mockResponseFalse
#         self.assertEqual(self.employeeTest.monthly_schedule('september'), "False")


from employee import Employee
import unittest
from unittest.mock import patch

# class EmployeeTests(unittest.TestCase):
#
#     def setUp(self):
#         self.empl = Employee('Nikita', 'Krutoholov', 1000)
#
#     @patch('employee.requests.get')
#     def test_monthly_schedule(self, mocked_get):
#         mocked_get.return_value.ok = True
#         res = self.empl.monthly_schedule('august')
#         self.assertIsNotNone(res)
#         self.assertNotEqual(res, 'Bad Response!')


import json
file_name = "employees.json"

# file = open("ReneeMontoyaApp/database/employees.json", 'r')
file = open("tests1/ReneeMontoyaApp/database" + file_name, 'r')
data = json.loads(file.read())
file.close()
print(data)