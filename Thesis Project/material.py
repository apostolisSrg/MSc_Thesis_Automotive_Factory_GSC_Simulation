from random import randrange


class Material:
    def __init__(self, material_id, material_type):
        self.material_id = material_id
        self.material_type = material_type
        self.history = []
        self.cost = randrange(300, 501)
        self.timestamp = randrange(1, 11)
        self.material_weight = randrange(700, 801)

    def __repr__(self):
        return f'Material({self.material_id}, "{self.material_type}", {self.history}, {self.cost}, {self.timestamp}, {self.material_weight})'
