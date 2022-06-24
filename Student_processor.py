from Student import Student

#create a function that loads the student data from the students.csv file
#create studnt objects and place in a list
#Return a list of student objects
def load_students():
    file = open("students.csv", "r")
    list_of_students = []
    line_number = 0
    for line in file:
        info = line.split(",")
        line_number = line_number + 1
        #To skip header line
        if line_number == 1:
            continue
        else:
            try: 
                list_of_students.append(Student(info[0], info[1], info[2], int(info[3]), float(info[4]), info[5]))
            except:
                print(f"Error on line {line_number} ")
                return "Error"
    
    return list_of_students

#just in case I need it
#I needed it
def print_student_data(list_of_students):
    for student in list_of_students:
        print(f"{student.get_first_name()} {student.get_last_name()}: {student.get_major()}")
        print(f"GPA: {student.get_gpa()}")
        print(f"Class: {student.get_class_level()}")
        print(f"ID Number: {student.get_id_number()}")
    
def sort_list(list_of_students):
    list_of_students.sort(key=lambda the_student: the_student.get_major())
    return list_of_students

def main():
    while True:   
        list_of_students = load_students()
        #In case of error
        if list_of_students == "Error":
            break
        else:
            sort_list(list_of_students)
            print_student_data(list_of_students)
            break 

main()