#Create a student Class with these attibutes
#First name
#Last name
#Major
#Class_level (freshman, sophmore, junior, senior)
#GPA
#ID number

#Create get/set methods where appropriate

class Student:
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number

    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_major(self):
        return self.__major

    def get_credit_hours(self):
        return self.__credit_hours

    def get_gpa(self):
        return self.__gpa

    def get_id_number(self):
        return self.__id_number

    def get_class_level(self):
        if int(self.__credit_hours) > 90:
            class_level = "senior"
        elif int(self.__credit_hours) > 60:
            class_level = "junior"
        elif int(self.__credit_hours) > 30:
            class_level = "sophmore"
        else:
            class_level = "freshman"
        return class_level
        
    
    
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_major(self, major):
        self.__major = major

    def set_credit_hours(self, new_credits):
        self.__credit_hours = new_credits

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def update_credit_hours(self, new_credits):
        self.__credit_hours += new_credits
