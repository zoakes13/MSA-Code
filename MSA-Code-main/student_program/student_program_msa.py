
print("Select option from Menu")
print("-----------------------")
print("1. Login")
print("2. Create User account")
   
while True:
    print()
    option = input("\nWould you like to login or create account? ")
    if option != "1" and option != "2":
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        break

if option == "1":
    while True:    
        #Get User input
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")
        file = open("users.txt", "r")
        user_found = False
        for line in file:
            credentials = line.split(",")
            if credentials[0] == user_name and credentials[1].rstrip() == user_pass:
                user_found = True
                break
        if user_found:
            print("User Logged in!")
            break
        else:
            print(f"User: {user_name} with password, {user_pass} not found.\n")

elif option == "2":
    while True:
        user_name = input("Please enter your user name (4 - 16 characters): ")
        user_pass = input("Please enter your password (6 - 12 characters): ")

        user_length = len(user_name)
        pass_length = len(user_pass)

        if (user_length >= 4 and user_length <= 16) and (pass_length >= 6 and pass_length <= 12):
            file = open("users.txt", "a")
            file.write(f"{user_name}, {user_pass}\n")
            file.close()
            print("Uesr Created")
            break
        else:
            print("ERROR: Invalid username or password length")

#Ask user how many students they have to enter
num_students =  input("Please enter number of students to enter grades for: ")
#Get students and scores. Store in arrays
student_array = []
scores_array = []
letter_grades = []

for counter in range(int(num_students)):
    stu_name = input("Enter student name: ")
    stu_score = int(input("Enter student score: "))

    #Add items to arrays
    student_array.append(stu_name)
    scores_array.append(int(stu_score))
            
    if stu_score >= 90:
        letter_grades.append("A") 
    elif stu_score >= 80:
        letter_grades.append("B") 
    elif stu_score >= 70:
        letter_grades.append("C") 
    elif stu_score >= 60:
        letter_grades.append("D") 
    else:
        letter_grades.append("F")

#Compute class average and lette grade
sum = 0  
for number in scores_array:
    sum = sum + number

avg_score = sum / len(scores_array)

print()    
#print student names, scores, letter grade
for index in range(len(student_array)):
    print(student_array[index]+":", scores_array[index],":", letter_grades[index])

#print a blank space for clarity
print()

#Print class average and average letter grade
print("Class Average:", avg_score)


