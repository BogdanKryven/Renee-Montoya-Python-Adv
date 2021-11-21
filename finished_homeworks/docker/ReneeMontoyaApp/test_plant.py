from fixtures11 import *

plant_test_json_file = 'tests/test_plant.json'
employees_test_json_file = 'tests/test_employees.json'


def open_test_plant_json():
    with open('database/tests/test_plant.json', 'w') as file:
        file.write('[]')
    Plant.file = 'tests/test_plant.json'


def open_test_employee_json():
    with open('database/tests/test_employees.json', 'w') as file:
        file.write('[]')
    Employee.file = 'tests/test_employees.json'


def test_plant_save(plant):
    open_test_plant_json()
    plant.save()
    assert 'id' in plant.get_by_id(plant.id)
    assert plant.name == plant.get_by_id(plant.id)['name']


def test_director(plant, employee_1, employee_2):
    open_test_plant_json()
    plant.save()
    open_test_employee_json()
    employee_1.save()
    employee_2.save()
    assert plant.director()['id'] == plant.get_by_id(plant.id)['director_id']
    assert plant.director()['id'] == employee_1.get_by_id(plant.id)['id']
    assert plant.director() == plant.get_file_data(file_name=employees_test_json_file)[0]
    assert plant.director()['name'] == plant.get_file_data(file_name=employees_test_json_file)[0]['name']


def test_get_plant_by_director_id(plant):
    open_test_plant_json()
    plant.save()
    assert plant.get_plant_by_director_id(plant.director_id)['director_id'] ==\
           plant.get_file_data(file_name=plant_test_json_file)[0]['director_id']
    assert plant.get_plant_by_director_id(plant.director_id) in plant.get_file_data(plant_test_json_file)
    assert plant.get_plant_by_director_id(9) not in plant.get_file_data(plant_test_json_file)
