from abc import ABC
import json


class Model(ABC):
    file = 'default.json'

    def _generate_dict(self):
        return self.__dict__

    def save(self):
        plant_in_dict_format = self._generate_dict()
        plants = self.get_file_data(self.file)
        plants.append(plant_in_dict_format)
        self.save_to_file(plants)

    @classmethod
    def get_by_id(cls, id_):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el['id'] == id_:
                return el

        raise Exception("Not found")

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data, indent=4)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()
