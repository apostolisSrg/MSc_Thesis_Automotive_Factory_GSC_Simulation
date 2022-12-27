from material import Material
from manufacturer import Manufacturer
from automobile import Automobile
from random import randrange, random, uniform

# Globals - Places
P1 = []
P2 = []
P3 = []
P4 = []
P5 = []
P6 = []
P7 = []
P8 = []
P9 = []
P10 = []
P11 = []
P12 = []
P13 = []
P14 = []
P15 = []
P16 = []
P17 = []
P18 = []
P19 = []
P20 = []
P21 = []

# A list that stores the ids for every token that is created. Unique value
ids = []

# Global lists which store every simulation result for each automobile_type
simulation_results_automobile_1 = []
simulation_results_automobile_2 = []
simulation_results_automobile_3 = []
simulation_results_automobile_4 = []

def print_petri_net():
    str = f"{40 * '-'} Next Event {103 * '-'}\n"
    str += f"P1 = {P1}\n"
    str += f"P2 = {P2}\n"
    str += f"P3 = {P3}\n"
    str += f"P4 = {P4}\n"
    str += f"P5 = {P5}\n"
    str += f"P6 = {P6}\n"
    str += f"P7 = {P7}\n"
    str += f"P8 = {P8}\n"
    str += f"P9 = {P9}\n"
    str += f"P10 = {P10}\n"
    str += f"P11 = {P11}\n"
    str += f"P12 = {P12}\n"
    str += f"P13 = {P13}\n"
    str += f"P14 = {P14}\n"
    str += f"P15 = {P15}\n"
    str += f"P16 = {P16}\n"
    str += f"P17 = {P17}\n"
    str += f"P18 = {P18}\n"
    str += f"P19 = {P19}\n"
    str += f"P20 = {P20}\n"
    str += f"P21 = {P21}"
    print(str)

# function that creates unique id for each new token that is generated
def next_id():
    if not ids:
        ids.append(1)
        return 1
    else:
        next = max(ids) + 1
        ids.append(next)
        return next


def t1_t2_t3_t4():
    # Because 4 transitions are enabled, we find a list which stores all timestamps in place P1
    # we define which one will fire each time first based on guards and on firing rules (tokens with minimum timestamps)
    timestamps = []
    for i in range(len(P1)):
        timestamps.append(P1[i].timestamp)

    for i in range(len(P1)):
        if P1[i].timestamp == min(timestamps):
            # t1
            if P1[i].material_type == "a":  # (G1)
                P1[i].cost += randrange(150, 201)
                P1[i].history.append("provincial supplier 1")
                P1[i].timestamp += randrange(2, 6)
                P2.append(P1.pop(i))
                return
            # t2
            elif P1[i].material_type == "c":  # (G2)
                P1[i].cost += randrange(450, 601)
                P1[i].history.append("county supplier 1")
                P1[i].timestamp += randrange(6, 16)
                P6.append(P1.pop(i))
                return
            # t3
            elif P1[i].material_type == "d":  # (G3)
                P1[i].cost += randrange(300, 401)
                P1[i].history.append("municipal supplier 2")
                P1[i].timestamp += randrange(4, 11)
                P5.append(P1.pop(i))
                return
            # t4
            else:  # (G4)
                P1[i].cost += randrange(150, 201)
                P1[i].history.append("provincial supplier 2")
                P1[i].timestamp += randrange(2, 6)
                P3.append(P1.pop(i))
                return


def t5_t6():
    timestamps = []
    for i in range(len(P2)):
        timestamps.append(P2[i].timestamp)

    for i in range(len(P2)):
        if P2[i].timestamp == min(timestamps):
            prop = random()  # Because there are no guards and both t5 and t6 can fire
            if prop <= 0.5:
                # t5
                P2[i].cost += randrange(150, 201)
                P2[i].history.append("municipal supplier 1")
                P2[i].timestamp += randrange(2, 6)
                P4.append(P2.pop(i))
                return
            else:
                # t6
                P2[i].cost += randrange(300, 401)
                P2[i].history.append("county supplier 1")
                P2[i].timestamp += randrange(4, 11)
                P6.append(P2.pop(i))
                return


def t7():
    timestamps = []
    for i in range(len(P3)):
        timestamps.append(P3[i].timestamp)

    for i in range(len(P3)):
        if P3[i].timestamp == min(timestamps):
            # t7
            P3[i].cost += randrange(150, 201)
            P3[i].history.append("municipal supplier 2")
            P3[i].timestamp += randrange(2, 6)
            P5.append(P3.pop(i))
            return


def t8():
    timestamps = []
    for i in range(len(P4)):
        timestamps.append(P4[i].timestamp)
    for i in range(len(P4)):
        if P4[i].timestamp == min(timestamps):
            # t8
            P4[i].cost += randrange(150, 201)
            P4[i].history.append("county supplier 1")
            P4[i].timestamp += randrange(2, 6)
            P6.append(P4.pop(i))
            return


def t9_t10():
    timestamps = []
    for i in range(len(P5)):
        timestamps.append(P5[i].timestamp)
    for i in range(len(P5)):
        if P5[i].timestamp == min(timestamps):
            # t9
            if P5[i].material_type == "b":  # (G5)
                P5[i].cost += randrange(150, 201)
                P5[i].history.append("county supplier 2")
                P5[i].timestamp += randrange(2, 6)
                P7.append(P5.pop(i))
                return
            else:  # (G6)
                P5[i].cost += randrange(150, 201)
                P5[i].history.append("county supplier 3")
                P5[i].timestamp += randrange(2, 6)
                P8.append(P5.pop(i))
                return


def t11_t12():
    timestamps = []
    for i in range(len(P6)):
        timestamps.append(P6[i].timestamp)
    for i in range(len(P6)):
        if P6[i].timestamp == min(timestamps):
            # t11
            if P6[i].material_type == "a":  # (G7)
                P6[i].cost += randrange(150, 201)
                P6[i].history.append("township supplier 1")
                P6[i].timestamp += randrange(2, 6)
                P9.append(P6.pop(i))
                return
            # t12
            else:  # (G8)
                P6[i].cost += randrange(150, 201)
                P6[i].history.append("township supplier 2")
                P6[i].timestamp += randrange(2, 6)
                P10.append(P6.pop(i))
                return


def t13():
    timestamps = []
    for i in range(len(P7)):
        timestamps.append(P7[i].timestamp)
    for i in range(len(P7)):
        if P7[i].timestamp == min(timestamps):
            # t13
            P7[i].cost += randrange(150, 201)
            P7[i].history.append("township supplier 3")
            P7[i].timestamp += randrange(2, 6)
            P11.append(P7.pop(i))
            return


def t14():
    timestamps = []
    for i in range(len(P8)):
        timestamps.append(P8[i].timestamp)
    for i in range(len(P8)):
        if P8[i].timestamp == min(timestamps):
            # t14
            P8[i].cost += randrange(150, 201)
            P8[i].history.append("township supplier 4")
            P8[i].timestamp += randrange(2, 6)
            P12.append(P8.pop(i))
            return


def t15():
    timestamps = []
    for i in range(len(P9)):
        timestamps.append(P9[i].timestamp)
    for i in range(len(P9)):
        if P9[i].timestamp == min(timestamps):
            # t15
            P9[i].cost += randrange(2500, 5001)
            P9[i].history.extend(["manufacturer 1", "automobile 1"])
            P9[i].timestamp += randrange(15, 21)
            material = P9.pop(i)
            manufacturer = P13.pop(0)
            automobile_1 = Automobile(material.material_id, material.material_type, manufacturer.manufacturer_id,
                                      manufacturer.manufacturer_type, material.history, material.timestamp,
                                      manufacturer.income, manufacturer.expenses, next_id(), "1")
            automobile_1.expenses += material.cost
            P17.append(automobile_1)
            return


def t16():
    timestamps = []
    for i in range(len(P10)):
        timestamps.append(P10[i].timestamp)
    for i in range(len(P10)):
        if P10[i].timestamp == min(timestamps):
            # t16
            P10[i].cost += randrange(2500, 5001)
            P10[i].history.extend(["manufacturer 2", "automobile 2"])
            P10[i].timestamp += randrange(15, 21)
            material = P10.pop(i)
            manufacturer = P14.pop(0)
            automobile_2 = Automobile(material.material_id, material.material_type, manufacturer.manufacturer_id,
                                      manufacturer.manufacturer_type, material.history, material.timestamp,
                                      manufacturer.income, manufacturer.expenses, next_id(), "2")
            automobile_2.expenses += material.cost
            P17.append(automobile_2)
            return


def t17():
    timestamps = []
    for i in range(len(P11)):
        timestamps.append(P11[i].timestamp)
    for i in range(len(P11)):
        if P11[i].timestamp == min(timestamps):
            # t17
            P11[i].cost += randrange(2500, 5001)
            P11[i].history.extend(["manufacturer 3", "automobile 3"])
            P11[i].timestamp += randrange(15, 21)
            material = P11.pop(i)
            manufacturer = P15.pop(0)
            automobile_3 = Automobile(material.material_id, material.material_type, manufacturer.manufacturer_id,
                                      manufacturer.manufacturer_type, material.history, material.timestamp,
                                      manufacturer.income, manufacturer.expenses, next_id(), "3")
            automobile_3.expenses += material.cost
            P17.append(automobile_3)
            return


def t18():
    timestamps = []
    for i in range(len(P12)):
        timestamps.append(P12[i].timestamp)
    for i in range(len(P12)):
        if P12[i].timestamp == min(timestamps):
            # t18
            P12[i].cost += randrange(2500, 5001)
            P12[i].history.extend(["manufacturer 4", "automobile 4"])
            P12[i].timestamp += randrange(15, 21)
            material = P12.pop(i)
            manufacturer = P16.pop(0)
            automobile_4 = Automobile(material.material_id, material.material_type, manufacturer.manufacturer_id,
                                      manufacturer.manufacturer_type, material.history, material.timestamp,
                                      manufacturer.income, manufacturer.expenses, next_id(), "4")
            automobile_4.expenses += material.cost
            P17.append(automobile_4)
            return


def t19_t02_t21_t22():
    # Because 4 transitions are enabled, we find a list which stores all timestamps in place P17
    # we define which one will fire each time first based on guards and on firing rules (tokens with minimum timestamps)
    timestamps = []
    for i in range(len(P17)):
        timestamps.append(P17[i].timestamp)

    for i in range(len(P17)):
        if P17[i].timestamp == min(timestamps):
            # t19
            if P17[i].automobile_type == "1":  # (G9)
                P17[i].expenses += randrange(150, 201)
                P17[i].history.append("distributor 1")
                P17[i].timestamp += randrange(3, 7)
                P18.append(P17.pop(i))
                return
            # t20
            elif P17[i].automobile_type == "2":  # (G10)
                P17[i].expenses += randrange(150, 201)
                P17[i].history.append("distributor 2")
                P17[i].timestamp += randrange(3, 7)
                P18.append(P17.pop(i))
                return
            # t21
            elif P17[i].automobile_type == "3":  # (G11)
                P17[i].expenses += randrange(150, 201)
                P17[i].history.append("distributor 3")
                P17[i].timestamp += randrange(3, 7)
                P18.append(P17.pop(i))
                return
            # t22
            else:  # (G12)
                P17[i].expenses += randrange(150, 201)
                P17[i].history.append("distributor 4")
                P17[i].timestamp += randrange(3, 7)
                P18.append(P17.pop(i))
                return


def t23_t24_t25_t26():
    # Because 4 transitions are enabled, we find a list which stores all timestamps in place P18
    # we define which one will fire each time first based on guards and on firing rules (tokens with minimum timestamps)
    timestamps = []
    for i in range(len(P18)):
        timestamps.append(P18[i].timestamp)

    for i in range(len(P18)):
        if P18[i].timestamp == min(timestamps):
            # t23
            if "distributor 1" in P18[i].history:  # (G13)
                P18[i].expenses += randrange(150, 201)
                P18[i].history.append("retailer 1")
                P18[i].timestamp += randrange(3, 7)
                P19.append(P18.pop(i))
                return
            # t24
            elif "distributor 2" in P18[i].history:  # (G14)
                P18[i].expenses += randrange(150, 201)
                P18[i].history.append("retailer 2")
                P18[i].timestamp += randrange(3, 7)
                P19.append(P18.pop(i))
                return
            # t25
            elif "distributor 3" in P18[i].history:  # (G15)
                P18[i].expenses += randrange(150, 201)
                P18[i].history.append("retailer 3")
                P18[i].timestamp += randrange(3, 7)
                P19.append(P18.pop(i))
                return
            # t22
            else:  # (G12)
                P18[i].expenses += randrange(150, 201)
                P18[i].history.append("retailer 4")
                P18[i].timestamp += randrange(3, 7)
                P19.append(P18.pop(i))
                return


def t27_t28_t29_t30():
    # Because 4 transitions are enabled, we find a list which stores all timestamps in place P19
    # we define which one will fire each time first based on guards and on firing rules (tokens with minimum timestamps)
    timestamps = []
    for i in range(len(P19)):
        timestamps.append(P19[i].timestamp)

    for i in range(len(P19)):
        if P19[i].timestamp == min(timestamps):
            # t27
            if "retailer 1" in P19[i].history:  # (G17)
                P19[i].income += randrange(7000, 9001)
                P19[i].history.append("customer 1")
                P19[i].timestamp += randrange(3, 7)
                P20.append(P19.pop(i))
                return
            # t28
            elif "retailer 2" in P19[i].history:  # (G18)
                P19[i].income += randrange(7000, 9001)
                P19[i].history.append("customer 2")
                P19[i].timestamp += randrange(3, 7)
                P20.append(P19.pop(i))
                return
            # t29
            elif "retailer 3" in P19[i].history:  # (G19)
                P19[i].income += randrange(7000, 9001)
                P19[i].history.append("customer 3")
                P19[i].timestamp += randrange(3, 7)
                P20.append(P19.pop(i))
                return
            # t22
            else:  # (G20)
                P19[i].income += randrange(7000, 9001)
                P19[i].history.append("customer 4")
                P19[i].timestamp += randrange(3, 7)
                P20.append(P19.pop(i))
                return


def t31_t32_t33_t34():
    # Because 4 transitions are enabled, we find a list which stores all timestamps in place P20
    # we define which one will fire each time first based on guards and on firing rules (tokens with minimum timestamps)
    timestamps = []
    for i in range(len(P20)):
        timestamps.append(P20[i].timestamp)

    for i in range(len(P20)):
        if P20[i].timestamp == min(timestamps):
            # t31
            if "customer 1" in P20[i].history:  # (G21)
                P20[i].history.append("recycling center 1")
                P20[i].timestamp += randrange(2, 6)
                P21.append(P20.pop(i))
                return
            # t28
            elif "customer 2" in P20[i].history:  # (G22)
                P20[i].history.append("recycling center 2")
                P20[i].timestamp += randrange(2, 6)
                P21.append(P20.pop(i))
                return
            # t29
            elif "customer 3" in P20[i].history:  # (G23)
                P20[i].history.append("recycling center 3")
                P20[i].timestamp += randrange(2, 6)
                P21.append(P20.pop(i))
                return
            # t22
            else:  # (G21)
                P20[i].history.append("recycling center 4")
                P20[i].timestamp += randrange(2, 6)
                P21.append(P20.pop(i))
                return


def t35_t36_t37_t38():
    # Because 4 transitions are enabled, we find a list which stores all timestamps in place P21
    # we define which one will fire each time first based on guards and on firing rules (tokens with minimum timestamps)
    timestamps = []
    for i in range(len(P21)):
        timestamps.append(P21[i].timestamp)

    for i in range(len(P21)):
        if P21[i].timestamp == min(timestamps):
            # t35
            if "recycling center 1" in P21[i].history:  # (G25)
                P21[i].history.append("recycled")
                P21[i].timestamp += randrange(10, 16)
                simulation_results_automobile_1.append(P21.pop(i))
                material_a = Material(next_id(), "a")
                material_a.cost -= int(uniform(0.5, 0.7) * material_a.cost)
                P1.append(material_a)
                manufacturer_1 = Manufacturer(next_id(), "1")
                P13.append(manufacturer_1)
                return
            # t36
            elif "recycling center 2" in P21[i].history:  # (G26)
                P21[i].history.append("recycled")
                P21[i].timestamp += randrange(10, 16)
                simulation_results_automobile_2.append(P21.pop(i))
                material_c = Material(next_id(), "c")
                material_c.cost -= int(uniform(0.5, 0.7) * material_c.cost)  # the material cost is lower because a percentage of it is recycled
                P1.append(material_c)
                manufacturer_2 = Manufacturer(next_id(), "2")
                P14.append(manufacturer_2)
                return

            # t37
            elif "recycling center 3" in P21[i].history:  # (G27)
                P21[i].history.append("recycled")
                P21[i].timestamp += randrange(10, 16)
                simulation_results_automobile_3.append(P21.pop(i))
                material_b = Material(next_id(), "b")
                material_b.cost -= int(uniform(0.5, 0.7) * material_b.cost)
                P1.append(material_b)
                manufacturer_3 = Manufacturer(next_id(), "3")
                P15.append(manufacturer_3)
                return
            # t38
            else:  # (G28)
                P21[i].history.append("recycled")
                P21[i].timestamp += randrange(10, 16)
                simulation_results_automobile_4.append(P21.pop(i))
                material_d = Material(next_id(), "d")
                material_d.cost -= int(uniform(0.5, 0.7) * material_d.cost)
                P1.append(material_d)
                manufacturer_4 = Manufacturer(next_id(), "4")
                P16.append(manufacturer_4)
                return
