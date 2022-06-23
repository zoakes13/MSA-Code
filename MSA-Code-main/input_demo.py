import math
#INPUT
#ask user for amount of wall to be painted
#ask user for price of paint per gallon
hourly_labor_cost = 62.25
unit_of_wall_area = 350
hours_of_labor_per_unit = 6

wall_area = float(input("What is the area of wall space in sqare ft: "))
paint_price = float(input("What is the price of paint per gallon? "))

#PROCESSING
#calculate to the gallons of paint needed
gallons_of_paint = math.ceil(wall_area / unit_of_wall_area)
#calculate to cost of the paint 
paint_cost = gallons_of_paint * paint_price
#calculate the number of hours needed
hours_of_labor = (wall_area / unit_of_wall_area) *hours_of_labor_per_unit
#calculate the labour cost
labor_cost = hourly_labor_cost * hours_of_labor
#calculate the total cost of the job 
total_cost = paint_cost + labor_cost

#OUTPUT
#print numer of gallons
print(f"Gallons of paint: {gallons_of_paint}")
#print cost of paint
print(f"Paint Cost: ${paint_cost}")
#print total hours
print(f"Total Hours: {hours_of_labor}")
#print total labour cost
print(f"Labor Cost: ${labor_cost}")
#print total job cost
#print(f"Total Cost: ${total_cost}")

#ask user if they want to do again