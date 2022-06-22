import os.path
from statistics import median

def get_file_name():
    while True:
        #prompt user to enter file name
        user_input = input("Please enter a file name: ")
        #make sure user entered a value. Re prompt if not
        if user_input == "":
            print("ERROR: please enter a value.\n")
            continue
        elif not os.path.exists(user_input):
            print("ERROR: File does not exist.\n")
            continue
        else:
            break
    #else return the value
    return user_input

#Function to load numbers from file into list
#Parameters: file name
#returns a list of numbers
def load_numbers_list(file_name):
    numbers_list = []
    #open the file
    file = open(file_name, "r")
    #read file line by line
    for number in file:
        #convert to int and append numbers to a list
        numbers_list.append(int(number))
    #return the list
    return numbers_list

def calculate_median_value(numbers_list):
    #sort the list
    numbers_list.sort()
    #determine if the list has an even or odd number of items using the len() function
    if (len(numbers_list) % 2 == 0):
        is_even = True
    else:
        is_even = False
    #if even find the two middle values and calculate the average of the two
    if is_even:
        index_1 = int(len(numbers_list) / 2)
        index_2 = index_1 - 1
        median = (numbers_list[index_1] + numbers_list[index_2]) / 2
    #if odd, return the middle value
    else:
        index = int((len(numbers_list) - 1) / 2)
        median = numbers_list[index]
 
    return median

def determine_modal_value(numbers_list):
    #Create a dictionary to store list values and frequencies
    modal_values ={}
    list_of_modal_values = []
    #Loop through list.
    for number in numbers_list:
        #If the number is in the dictionary then add 1 to its value
        if number in modal_values:
            modal_values[number] += 1
        #If number not in dictionary then insert as key in dictionary with value 1
        else:
            modal_values[number] = 1
    #Determine the largest value in the dictionary
    list_values = modal_values.values()
    max_value = max(list_values)
    #Append those keys with the largest values to a list 
    for key in modal_values:
        if modal_values[key] == max_value:
            list_of_modal_values.append(key)
    #Return list of modal value(s)
    return list_of_modal_values

def calculate_sum(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = sum + number
    return sum

def calculate_max(numbers_list):
    max = 0
    for number in numbers_list:
        if number > max:
            max = number
    return max

def calculate_min(numbers_list):
    min = 0
    for number in numbers_list:
        if number < min:
            min = number
    return min

def print_values(file_name, sum, count, average, maximum, minimum, range, median, modal_values):
    print(f"File Name: {file_name}")
    print(f"Sum: {sum}")
    print(f"Count: {count}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Range: {range}")
    print(f"Median: {median}")
    print(f"Mode: {modal_values}")

def ask_repeat():
    while True:
        repeat = input("Would you like to calculate another file? Y/N? ")
        if repeat == "Y" or repeat == "y":
            repeat = True
            return repeat
        if repeat == "N" or repeat == "n":
            print("Goodbye!")
            repeat = False
            return repeat
        else:
            print("ERROR: Please input Y or N.")

def main():
    loop = True
    while loop:
        #ask user to enter filename and open that file
        file_name = get_file_name()
        
        #load number from file into a list
        list_of_numbers = load_numbers_list(file_name)

        #check the length of the list
        if len(list_of_numbers) == 0:
            print("File was empty")
        elif len(list_of_numbers) == 1:
            print("Only one number in file")
        else:
            median = calculate_median_value(list_of_numbers)
            modal_values = determine_modal_value(list_of_numbers)
            sum = calculate_sum(list_of_numbers)
            count = len(list_of_numbers)
            average = sum / count
            maximum = calculate_max(list_of_numbers)
            minimum = calculate_min(list_of_numbers)
            range = maximum - minimum

            print_values(file_name, sum, count, average, maximum, minimum, range, median, modal_values)

            loop = ask_repeat()

main()