#Create a student Class with these attibutes
#First name
#Last name
#Major
#Class_level (freshman, sophmore, junior, senior)
#GPA
#ID number

#Create get/set methods where appropriate

class Student:
    def __init__(self, first_name, last_name, major, class_level, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__class_level = class_level
        self.__gpa = gpa
        self.__id_number = id_number

    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_major(self):
        return self.__major

    def get_class_level(self):
        return self.__class_level

    def get_gpa(self):
        return self.__gpa

    def get_id_number(self):
        return self.__id_number

    
    
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_major(self, major):
        self.__major = major

    def set_class_level(self, class_level):
        self.__class_level = class_level

    def set_gpa(self, gpa):
        self.__gpa = gpa

student1 = Student("Kyle", "Roberts", "Explosives 101", "Sophmore", 3.8, 123456789)
print(student1.get_first_name())
print(student1.get_last_name())
print(student1.get_id_number())
student1.set_class_level("Junior")
print(student1.get_class_level())
