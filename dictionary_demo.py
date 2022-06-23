
#Ask user to enter number number of students
num_students = int(input("How many students do you have data for: "))

#Create a list for the student dictionaries
student_list = []

#Ask user to enter the student names and number scores and store in a dictionary
for index in range(num_students):
    student_name = input(f"Enter student {index + 1} name: ")
    student_score = int(input(f"Enter student {index + 1} score: "))
    
    #place the student dictionary in the student list
    student_list.append({"name": student_name, "score": student_score})

#print the student data to the console
for student in student_list:
    print(f"{student['name']}: {student['score']}")

print("\n\n")
for index in range(len(student_list)):
    print(f"{student_list[index]['name']}: {student_list[index]['score']}")
