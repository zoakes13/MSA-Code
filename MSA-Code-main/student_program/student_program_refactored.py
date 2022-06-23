def print_start_menu():
    print("\nSelect option from Menu")
    print("-----------------------")
    print("1. Login")
    print("2. Create User account")
    print("3. Exit.")
    return

def get_user_option():
    while True:
        print()
        option = input("\nWould you like to login or create an account? ")
        if (option != "1") and (option != "2") and (option != "3"):
            print("\nERROR: Enter a 1 or 2 or 3\n")
            continue
        else:
            break
    return option

def login_user():
    while True:
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")
        #login user
        file = open("users.txt", "r")
        user_found = False
        for line in file:
            credentials = line.split(", ")
            if credentials[0] == user_name and credentials[1].rstrip() == user_pass:
                user_found = True
                break
        if user_found:
            print(f"{user_name} successfully logged in!\n")
            return True
        else:
            print(f"User: {user_name} with password, {user_pass} not found.\n")

def get_valid_username_or_password(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        input_length = len(user_input)
        if (input_length >= min_length) and (input_length <= max_length):
            break
        else:
            print("ERROR: Input length invalid!\n")
            continue
    return user_input

def create_user():
    user_created = False
    while not user_created:
        user_name = get_valid_username_or_password("Please enter your user name (4 - 16 characters): ", 4, 16)
        user_pass = get_valid_username_or_password("Please enter your password (6 - 12 characters): ", 6, 12)

        try:
            file = open("users.txt", "a")
            file.write(f"{user_name}, {user_pass}\n")
        except:
            print("ERROR creating user\n")
            continue
        else:
            print(f"User {user_name} created!\n")
            user_created = True
        finally:
            file.close()   
    
    return True

def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
        except:
            print("ERROR: input must be a number.\n")
        else:
            break

    return user_input

def load_student_and_scores_list(number_of_students):
    student_names_list, scores_list = [], []

    for counter in range(number_of_students):
        stu_name = input("\nEnter student name: ")
        stu_score = get_integer_input("Enter student score: ")

        #Add items to arrays
        student_names_list.append(stu_name)
        scores_list.append(stu_score)

    return student_names_list, scores_list

def load_letter_grades(scores_list):
    list_of_grades = []
    for score in scores_list:
        if score >= 90:
            list_of_grades.append("A") 
        elif score >= 80:
            list_of_grades.append("B") 
        elif score >= 70:
            list_of_grades.append("C") 
        elif score >= 60:
            list_of_grades.append("D") 
        else:
            scores_list.append("F")
    return list_of_grades

def calculate_avg_score(list_of_scores):
    sum = 0  
    for number in list_of_scores:
        sum = sum + number

    avg_score = sum / len(list_of_scores)
    return avg_score

def print_output(student_list, scores_list, letter_grades, average_score):   
    #print student names, scores, letter grade
    print()
    for index in range(len(student_list)):
        print(student_list[index]+":", scores_list[index],":", letter_grades[index])

    #Print class average and average letter grade
    print("\nClass Average:", average_score)
    return

def main():
    logged_in = False
    while True:
        #print Menu
        print_start_menu()
        #get menu selection
        user_option = get_user_option()

        if user_option == "1":
            logged_in = login_user()
        elif user_option == "2":
            create_user()
        else:
            print("Goodbye!")
            break

        #Ask user how many students they have to enter
        num_students =  get_integer_input("Please enter number of students to enter grades for: ")
        #Get students and scores. Store in arrays
        student_list, scores_list, letter_grades = [], [], []

        #Load student and score list
        student_list, scores_list = load_student_and_scores_list(num_students)

        #Load Letter grades
        letter_grades = load_letter_grades(scores_list)

        #Compute class average and lette grade
        avg_score = calculate_avg_score(scores_list)

        #print output
        print_output(student_list, scores_list, letter_grades, avg_score)
        
        
main()
