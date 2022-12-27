from manufacturer import Manufacturer
from material import Material
from automobile import Automobile
from transitions import *
from other_functions import *

def main():
    print(f"+{64 * '-'}+")
    print(f"|{('Welcome to the Colored Petri Net Optimized Model Simulation').center(64)}|")
    print(f"|{('Thesis Implementation by Saroglou Apostolos').center(64)}|")
    print(f"+{64 * '-'}+")
    print("")
    simulations = valid_user_input()
    # Initialize Black Tokens
    material_a = Material(next_id(), "a")
    material_b = Material(next_id(), "b")
    material_c = Material(next_id(), "c")
    material_d = Material(next_id(), "d")
    P1.append(material_a)
    P1.append(material_b)
    P1.append(material_c)
    P1.append(material_d)
    # Initialize Red Tokens
    manufacturer_1 = Manufacturer(next_id(), "1")
    manufacturer_2 = Manufacturer(next_id(), "2")
    manufacturer_3 = Manufacturer(next_id(), "3")
    manufacturer_4 = Manufacturer(next_id(), "4")
    P13.append(manufacturer_1)
    P14.append(manufacturer_2)
    P15.append(manufacturer_3)
    P16.append(manufacturer_4)
    # events / transitions start to take place
    for i in range(simulations):
        print("")
        print(f"{40 * '~'} Simulation {i + 1} {210 * '~'}\n")
        print_petri_net()
        if P1:
            while len(P1) >= 1:
                t1_t2_t3_t4()
                print_petri_net()
        if P2:
            while len(P2) >= 1:
                t5_t6()
                print_petri_net()
        if P3:
            while len(P3) >= 1:
                t7()
                print_petri_net()
        if P4:
            while len(P4) >= 1:
                t8()
                print_petri_net()
        if P5:
            while len(P5) >= 1:
                t9_t10()
                print_petri_net()
        if P6:
            while len(P6) >= 1:
                t11_t12()
                print_petri_net()
        if P7:
            while len(P7) >= 1:
                t13()
                print_petri_net()
        if P8:
            while len(P8) >= 1:
                t14()
                print_petri_net()
        if P9 and P13:
            while len(P9) >= 1 and len(P13) >= 1:
                t15()
                print_petri_net()
        if P10 and P14:
            while len(P10) >= 1 and len(P14) >= 1:
                t16()
                print_petri_net()
        if P11 and P15:
            while len(P11) >= 1 and len(P15) >= 1:
                t17()
                print_petri_net()
        if P12 and P16:
            while len(P12) >= 1 and len(P16) >= 1:
                t18()
                print_petri_net()
        if P17:
            while len(P17) >= 1:
                t19_t02_t21_t22()
                print_petri_net()
        if P18:
            while len(P18) >= 1:
                t23_t24_t25_t26()
                print_petri_net()
        if P19:
            while len(P19) >= 1:
                t27_t28_t29_t30()
                print_petri_net()
        if P20:
            while len(P20) >= 1:
                t31_t32_t33_t34()
                print_petri_net()
        if P21:
            while len(P21) >= 1:
                t35_t36_t37_t38()
                print_petri_net()

    save_to_txt_v1("simulation-results.txt", simulations, simulation_results_automobile_1, simulation_results_automobile_2, simulation_results_automobile_3, simulation_results_automobile_4)
    save_to_txt_v2("simulation-results-automobile-1.txt", simulation_results_automobile_1)
    save_to_txt_v2("simulation-results-automobile-2.txt", simulation_results_automobile_2)
    save_to_txt_v2("simulation-results-automobile-3.txt", simulation_results_automobile_3)
    save_to_txt_v2("simulation-results-automobile-4.txt", simulation_results_automobile_4)
    automobile_statistics("statistics.txt", simulations, simulation_results_automobile_1, simulation_results_automobile_2, simulation_results_automobile_3,simulation_results_automobile_4 )
    print("\nSuccessful Process!")
    print("\nThe results of all simulations are saved to file 'simulation-results.txt'.\n"
            "The results of all simulations for each Automobile are saved to files 'simulation-results-automobile-1.txt',\n"
          "'simulation-results-automobile-2.txt', 'simulation-results-automobile-3.txt', 'simulation-results-automobile-4.txt' respectively.\n"
          "The file 'statistics.txt' summarizes statistics for all simulations.")
try:
    main()
except KeyboardInterrupt as f:
    print("\n\n--There was an unexpected termination of the program--")