from models.plant import Plant
from models.employee import Employee
import json


class Menu:

    def __init__(self, menu_flag):
        self.menu_flag = menu_flag

    @staticmethod
    def run():
        Menu.choice()
        menu_flag = int(input("Input your choice: "))
        start = Menu(menu_flag)
        start.logic()

    @staticmethod
    def choice():
        print(
            "Choose a menu item by number: \n" +
            "1. Add new Plant \n" +
            "2. Add new Employee \n" +
            "3. Get plant by id \n" +
            "4. Get employee by id \n" +
            "5. Get director id by employee email \n"
        )

    @staticmethod
    def get_director_id_by_employee_email(input_email):
        file_employees = open("database/employees.json", 'r')
        file_plant = open("database/plants.json", 'r')
        data_employees = json.loads(file_employees.read())
        data_plants = json.loads(file_plant.read())
        file_employees.close()
        file_plant.close()

        for el_employees in data_employees:
            if el_employees['email'] == input_email:
                id_ = el_employees['department_id']
                for el_plants in data_plants:
                    if el_plants['id'] == id_:
                        return f"Director id: {el_plants['director_id']}\n"

    def logic(self):
        if self.menu_flag == 1:
            id_ = int(input("ID: "))
            location = input("Location: ")
            name = input("Name: ")
            director_id = int(input("Director ID: "))
            plant = Plant(id_, location, name, director_id)
            plant.save()

        elif self.menu_flag == 2:
            id_ = int(input("ID: "))
            name = input("Name: ")
            email = input("Email: ")
            department_type = input("Department Type: ")
            department_id = int(input("Department id: "))
            employee = Employee(id_, name, email, department_type, department_id)
            employee.save()

        elif self.menu_flag == 3:
            id_ = int(input("ID: "))
            plant = Plant.get_by_id(id_)
            print(plant)

        elif self.menu_flag == 4:
            id_ = int(input("ID: "))
            employee = Employee.get_by_id(id_)
            print(employee)

        elif self.menu_flag == 5:
            email = str(input("Employee email: "))
            director = Menu.get_director_id_by_employee_email(email)
            print(director)
