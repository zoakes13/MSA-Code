import random

my_list = [6, 5, 3, 7, 8, 4, 2, 5, 11, 43, 17, 27, 99, 62, 61, 51, 47]
print(my_list[0])
print(my_list[1])

print("Loop through List\n")
for item in my_list:
    print(item)

#Item 1: 6
#Item 2: 5
#Get the number of items in the list
number_of_items = len(my_list)
for index in range(number_of_items):
    print(f"Item {index}: {my_list[index]}")

print("Sum Values List\n")
total = 0
for number in my_list:
    total = total + number
print(f"Total: {total}")

print("Range Function of Loop\n")
for index in range(5, number_of_items, 2):
    print(f"Item {index}: {my_list[index]}")

print("Largest Value\n")
max_value = my_list[0]
for number in my_list:
    if number < max_value:
        max_value = number
print(f"Largest Values: {max_value}")

print("Insert Random values\n")
for count in range(3):
    random_value = random.randint(1, 100)
    my_list.append(random_value)

print(my_list)

print("Insert Values From File\n")
#open the file
values_file = open("values.txt", "r")
#read values from the file line by line
for line in values_file:
    #append values to list
    my_list.append(int(line))

#close the file
values_file.close()
print(my_list)


