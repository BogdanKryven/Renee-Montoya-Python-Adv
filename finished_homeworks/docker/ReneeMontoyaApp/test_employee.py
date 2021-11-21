import unittest
from unittest.mock import patch
from fixtures11 import *

employees_test_json_file = 'tests/test_employees.json'


def open_test_employee_json():
    with open('database/tests/test_employees.json', 'w') as file:
        file.write('[]')
    Employee.file = 'tests/test_employees.json'


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_1 = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)
        self.employee_2 = Employee(2, "Test not tester", "blablabla@gmail.com", "factory", 2)

    def test_generate_dict(self):
        self.assertIn('id', self.employee_1._generate_dict())
        self.assertEqual(self.employee_1._generate_dict()['id'], 1)
        self.assertEqual(self.employee_1._generate_dict()['department_type'], 'plant')

    @patch('models.Employee.get_file_data')
    def test_get_by_id(self, fileDataMock):
        fileDataMock.return_value = [{"id": 1, "email": "lubomur.luzhnuy@gmail.com", "name": "Liubomyr Luzhnyi",
                                      "department_type": "plant", "department_id": 1},
                                     {"id": 2, "email": "anton@gmail.com", "name": "Anton",
                                      "department_type": "plant", "department_id": 2}]
        self.assertEqual(self.employee_1.get_by_id(1)['email'], "lubomur.luzhnuy@gmail.com")
        self.assertIn('id', self.employee_1.get_by_id(1))

    def test_department(self):
        Plant.file = 'tests/test_plant.json'
        open_test_employee_json()
        self.employee_1.save()
        self.employee_2.save()
        self.assertEqual(self.employee_2.department(), None)
        self.assertEqual(self.employee_1.department(), Plant.get_by_id(self.employee_1.department_id))


def test_department(plant, employee_1, employee_2):
    Plant.file = 'tests/test_plant.json'
    open_test_employee_json()
    employee_1.save()
    employee_2.save()
    assert employee_2.department() is None
    assert employee_1.department() == Plant.get_by_id(employee_1.department_id)
