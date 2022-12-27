class Manufacturer:
    def __init__(self, manufacturer_id, manufacturer_type):
        self.manufacturer_id = manufacturer_id
        self.manufacturer_type = manufacturer_type
        self.income = 0
        self.expenses = 0

    def __repr__(self):
        return f'Manufacturer({self.manufacturer_id}, "{self.manufacturer_type}", {self.income}, {self.expenses})'
