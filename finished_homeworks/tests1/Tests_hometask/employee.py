import requests
import pytest


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    def fullname_and_email(self):
        return f"{self.fullname} \n{self.email}"

    def monthly_schedule(self, month):
        response = requests.get(f"https://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"


EMPLOYEE = Employee("Bohdan", "Kryven", 100)


@pytest.fixture()
def employee_email():
    return EMPLOYEE.email


@pytest.fixture()
def employee_fullname():
    return EMPLOYEE.fullname


@pytest.fixture()
def employee_raise():
    return EMPLOYEE.apply_raise


@pytest.fixture()
def employee_fullname_and_email():
    return EMPLOYEE.fullname_and_email

