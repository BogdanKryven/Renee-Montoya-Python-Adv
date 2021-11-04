import json


class Plant:

    file = "bla.json"

    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def _generate_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @staticmethod
    def get_file_data():
        file = open("bla.json", 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data, indent=4)
        file = open(self.file, 'w')
        file.write(data)
        file.close()

    def save(self):
        employees_in_dict_format = self._generate_dict()
        employees = self.get_file_data()
        employees.append(employees_in_dict_format)
        self.save_to_file(employees)


a = Plant(7, "Bohdan")
# a.save()
print(a.id)
print(a.name)
