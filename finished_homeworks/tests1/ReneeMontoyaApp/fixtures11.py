from pytest import fixture
from models import Plant, Employee


@fixture()
def plant():
    return Plant(1, 'Kiev', "Test", 1)


@fixture()
def employee_1():
    return Employee(1, "Bohdan", "bohdan1108@gmail.com", "plant", 1)


@fixture()
def employee_2():
    return Employee(2, "Roman", "roman@gmail.com", "ne_plant", 1)
