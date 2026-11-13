# Name: Grant Tanski
# Date: 2026-11-13
# Program: Pizza Party Planner
# Description: Plans how many whole pizzas are needed, how many extra slices there are, and what the cost will be.

# Constants
SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25

# Asking for input to assign values to variables
host_name = str(input("Host name: "))
people_amount = int(input("Number of people: "))
slices_per_person = int(input("Slices per person: "))

# Processing values to display in output
total_slices = people_amount * slices_per_person
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA
total_cost = whole_pizzas * PIZZA_PRICE + extra_slices * SLICE_PRICE
cost_per_person = total_cost / people_amount

# Displaying in output
print(f"=== Pizza Plan for {host_name}\'s Party ===")
print(f"Slices needed:    {total_slices}")
print(f"Whole pizzas:     {whole_pizzas}")
print(f"Extra slices:     {extra_slices}")
print(f"Total cost:       ${total_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")
