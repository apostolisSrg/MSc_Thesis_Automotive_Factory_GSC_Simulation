from material import Material
from manufacturer import Manufacturer


class Automobile(Material, Manufacturer):
    def __init__(self, material_id, material_type, manufacturer_id, manufacturer_type, history, timestamp,
                 income, expenses, id, automobile_type):
        Material.__init__(self, material_id, material_type)
        Manufacturer.__init__(self, manufacturer_id, manufacturer_type)
        self.history = history
        self.timestamp = timestamp
        self.income = income
        self.expenses = expenses
        self.id = id
        self.automobile_type = automobile_type

    def __str__(self):
        sp1 = []
        sp2 = []
        sp3 = []
        st = f"+{39 * '-'}" + f"Automobile {self.automobile_type}" + f"{39 * '-'}+" + "\n"
        st += f"| {('ID: ' + str(self.id)).ljust(89)}|" + "\n"
        st += f"| {('Timestamp: ' + str(self.timestamp)).ljust(89)}|" + "\n"
        st += f"| {('Material: ' + self.material_type).ljust(89)}|" + "\n"
        st += f"| {('Material Weight: ' + str(self.material_weight)).ljust(89)}|" + "\n"
        st += f"| {('Manufacturer: ' + self.manufacturer_type).ljust(89)}|" + "\n"
        for i in range(len(self.history)):
            if i < 3:
                sp1.append(self.history[i])
            elif 3 <= i <= 7:
                sp2.append(self.history[i])
            else:
                sp3.append(self.history[i])
        st1 = " -> ".join(sp1)
        st2 = " -> ".join(sp2)
        st3 = " -> ".join(sp3)
        st += f"| {('History: ' + st1 + ' ->').ljust(89)}|" + "\n" + "|"
        if st3:
            st += f" {(st2 + ' ->').ljust(89)}|" + "\n"
            st += "|" + f" {st3.ljust(89)}|" + "\n"
        else:
            st += f" {st2 .ljust(89)}|" + "\n"

        st += f"| {('Income: ' + str(self.income)).ljust(89)}|" + "\n"
        st += f"| {('Expenses: ' + str(self.expenses)).ljust(89)}|" + "\n"
        st += f"| {('Profits: ' + str(self.get_profits())).ljust(89)}|" + "\n"
        st += f"+{90 * '-'}+"
        return st

    def __repr__(self):
        return f'Automobile({self.material_id}, "{self.material_type}",' \
               f' "{self.manufacturer_type}", {self.manufacturer_id},' \
               f' {self.history}, {self.timestamp}, {self.income},' \
               f' {self.expenses}, {self.id}, "{self.automobile_type}")'

    def get_profits(self):
        return self.income - self.expenses
