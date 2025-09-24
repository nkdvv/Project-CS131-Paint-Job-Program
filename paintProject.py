# Nikki Davis & Ridge Torregosa
# Sept. 23rd, 2025
# Paint Project

import math

# STEP ONE
# Request user input
width = float(input("Wall width: "))
height = float(input("Wall height: "))
cost = float(input("Cost of one paint can: "))

# Output
area = float(width * height)
print(f'Wall area: {area: .1f} sq ft') # needs format specifier

# STEP TWO 
# Calculate the amount of paint by the third decimal
# * one gallon of paint covers 350 sq ft *
coverage = float(area/350)

# Output
print(f'Paint needed: {coverage: .3f} gallons.')

# STEP THREE
# Calculate the number of gallon cans needed to paint the wall area

totalCans = math.ceil(coverage)

# Output
print("Cans needed: ", totalCans, "cans(s)")

# STEP FOUR
# Calculate and output the paint cost, sales tax of 7%, and total cost. 
SALES_TAX = 0.07
cost2 = float(cost * totalCans)
tax = float(cost2 * SALES_TAX)
totalCost = float(cost2 + tax)

# Output
print(f'Paint cost: ${cost: .2f}')
print(f'Sales tax: ${tax: .2f}')
print(f'Total cost: ${totalCost: .2f}')
