"""User should enter a positive integer for the number of simulations. This function
controls the user input"""
def valid_user_input():
    while True:
        try:
            user_input = input("Type the number of Simulations you wish to run: ")
            if user_input == "":
                raise ValueError("No digits entered!")
            elif user_input[0] == "-":
                st = user_input[1:]
                if st == "":
                    raise ValueError("No digits entered!")
                elif not st.isdigit():
                    raise ValueError("Wrong Input. Only digits!")
                else:
                    raise ValueError("Wrong Input. Give a positive integer!")
            elif not user_input.isdigit():
                raise ValueError("Wrong Input. Only digits!")
            else:
                user_input = int(user_input)
                return user_input
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)

"""Saves the simulation results for Automobiles in .txt file"""
def save_to_txt_v1(filename, number_of_simulations, simulation_results_automobile_1, simulation_results_automobile_2, simulation_results_automobile_3, simulation_results_automobile_4,):
    with open(filename, 'w') as f:
        for i in range(number_of_simulations):
            f.write("\n")
            f.write(f"{40 * '~'}" + f" Simulation {i + 1} " + f"{40 * '~'}")
            f.write("\n\n")
            f.write(str(simulation_results_automobile_1[i]))
            f.write("\n")
            f.write(str(simulation_results_automobile_2[i]))
            f.write("\n")
            f.write(str(simulation_results_automobile_3[i]))
            f.write("\n")
            f.write(str(simulation_results_automobile_4[i]))

"""Saves the simulation results for each Automobile in .txt file"""
def save_to_txt_v2(filename, simulation_results_automobile):
    with open(filename, 'w') as f:
        for i in range(len(simulation_results_automobile)):
            f.write(f"{40 * '~'}" + f" Simulation {i + 1} " + f"{40 * '~'}")
            f.write("\n\n")
            f.write(str(simulation_results_automobile[i]))
            f.write("\n\n")


"""Draws important statistics for each Automobile depending on the number of simulations"""
def automobile_statistics(filename, number_of_simulations, simulation_results_automobile_1, simulation_results_automobile_2, simulation_results_automobile_3, simulation_results_automobile_4):
        total_income_1 = 0
        total_expenses_1 = 0
        total_weight_1 = 0
        total_profits_1 = 0
        total_timestamp_1 = 0
        for i in range(len(simulation_results_automobile_1)):
            total_income_1 += simulation_results_automobile_1[i].income
            total_weight_1 += simulation_results_automobile_1[i].material_weight
            total_expenses_1 += simulation_results_automobile_1[i].expenses
            total_profits_1 += simulation_results_automobile_1[i].get_profits()
            total_timestamp_1 += simulation_results_automobile_1[i].timestamp

        total_income_2 = 0
        total_expenses_2 = 0
        total_weight_2 = 0
        total_profits_2 = 0
        total_timestamp_2 = 0
        for i in range(len(simulation_results_automobile_2)):
            total_income_2 += simulation_results_automobile_2[i].income
            total_weight_2 += simulation_results_automobile_2[i].material_weight
            total_expenses_2 += simulation_results_automobile_2[i].expenses
            total_profits_2 += simulation_results_automobile_2[i].get_profits()
            total_timestamp_2 += simulation_results_automobile_2[i].timestamp

        total_income_3 = 0
        total_expenses_3 = 0
        total_weight_3 = 0
        total_profits_3 = 0
        total_timestamp_3 = 0
        for i in range(len(simulation_results_automobile_3)):
            total_income_3 += simulation_results_automobile_3[i].income
            total_weight_3 += simulation_results_automobile_3[i].material_weight
            total_expenses_3 += simulation_results_automobile_3[i].expenses
            total_profits_3 += simulation_results_automobile_3[i].get_profits()
            total_timestamp_3 += simulation_results_automobile_3[i].timestamp

        total_income_4 = 0
        total_expenses_4 = 0
        total_weight_4 = 0
        total_profits_4 = 0
        total_timestamp_4 = 0
        for i in range(len(simulation_results_automobile_4)):
            total_income_4 += simulation_results_automobile_4[i].income
            total_weight_4 += simulation_results_automobile_4[i].material_weight
            total_expenses_4 += simulation_results_automobile_4[i].expenses
            total_profits_4 += simulation_results_automobile_4[i].get_profits()
            total_timestamp_4 += simulation_results_automobile_4[i].timestamp

        with open(filename,'w') as f:
                f.write("Statistics Comparison\n")
                f.write(f"Simulations: {number_of_simulations}")
                f.write("\n\n")
                f.write(f"--Automobile 1--\n")
                f.write("Manufacturer: 1\n")
                f.write("Material: a\n")
                f.write(f"Total Material Weight: {total_weight_1}\n")
                f.write(f"AVG Material Weight: {round(total_weight_1 / number_of_simulations, 3)}\n")
                f.write(f"Total Income: {total_income_1}\n")
                f.write(f"AVG Income: {round(total_income_1 / number_of_simulations, 3)}\n")
                f.write(f"Total Expenses: {total_expenses_1}\n")
                f.write(f"AVG Expenses: {round(total_expenses_1 / number_of_simulations, 3)}\n")
                f.write(f"Total Profits: {total_profits_1}\n")
                f.write(f"AVG Profits: {round(total_profits_1 / number_of_simulations, 3)}\n")
                f.write(f"Total Time: {total_timestamp_1}\n")
                f.write(f"AVG Time: {round(total_timestamp_1 / number_of_simulations, 3)}\n")
                f.write("\n\n")
                f.write(f"--Automobile 2--\n")
                f.write("Manufacturer: 2\n")
                f.write("Material: c\n")
                f.write(f"Total Material Weight: {total_weight_2}\n")
                f.write(f"AVG Material Weight: {round(total_weight_2 / number_of_simulations, 3)}\n")
                f.write(f"Total Income: {total_income_2}\n")
                f.write(f"AVG Income: {round(total_income_2 / number_of_simulations, 3)}\n")
                f.write(f"Total Expenses: {total_expenses_2}\n")
                f.write(f"AVG Expenses: {round(total_expenses_2 / number_of_simulations, 3)}\n")
                f.write(f"Total Profits: {total_profits_2}\n")
                f.write(f"AVG Profits: {round(total_profits_2 / number_of_simulations, 3)}\n")
                f.write(f"Total Time: {total_timestamp_2}\n")
                f.write(f"AVG Time: {round(total_timestamp_2 / number_of_simulations, 3)}\n")
                f.write("\n\n")
                f.write(f"--Automobile 3--\n")
                f.write("Manufacturer: 3\n")
                f.write("Material: b\n")
                f.write(f"Total Material Weight: {total_weight_3}\n")
                f.write(f"AVG Material Weight: {round(total_weight_3 / number_of_simulations, 3)}\n")
                f.write(f"Total Income: {total_income_3}\n")
                f.write(f"AVG Income: {round(total_income_3 / number_of_simulations, 3)}\n")
                f.write(f"Total Expenses: {total_expenses_3}\n")
                f.write(f"AVG Expenses: {round(total_expenses_3 / number_of_simulations, 3)}\n")
                f.write(f"Total Profits: {total_profits_3}\n")
                f.write(f"AVG Profits: {round(total_profits_3 / number_of_simulations, 3)}\n")
                f.write(f"Total Time: {total_timestamp_3}\n")
                f.write(f"AVG Time: {round(total_timestamp_3 / number_of_simulations, 3)}\n")
                f.write("\n\n")
                f.write(f"--Automobile 4--\n")
                f.write("Manufacturer: 4\n")
                f.write("Material: d\n")
                f.write(f"Total Material Weight: {total_weight_4}\n")
                f.write(f"AVG Material Weight: {round(total_weight_4 / number_of_simulations, 3)}\n")
                f.write(f"Total Income: {total_income_4}\n")
                f.write(f"AVG Income: {round(total_income_4 / number_of_simulations, 3)}\n")
                f.write(f"Total Expenses: {total_expenses_4}\n")
                f.write(f"AVG Expenses: {round(total_expenses_4 / number_of_simulations, 3)}\n")
                f.write(f"Total Profits: {total_profits_4}\n")
                f.write(f"AVG Profits: {round(total_profits_4 / number_of_simulations, 3)}\n")
                f.write(f"Total Time: {total_timestamp_4}\n")
                f.write(f"AVG Time: {round(total_timestamp_4 / number_of_simulations, 3)}\n")
