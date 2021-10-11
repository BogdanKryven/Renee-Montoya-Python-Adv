from framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, id_, location, name, director_id):
        self.id = id_
        self.location = location
        self.name = name
        self.director_id = director_id
