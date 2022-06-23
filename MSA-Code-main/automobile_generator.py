from automobile import Automobile

def print_data(automobile_object):
    print("\nAuto Data")
    print(automobile_object.get_make())
    print(automobile_object.get_model())
    print(automobile_object.get_vin())
    print(automobile_object.get_color())
    print(automobile_object.get_age())

def main():
    #create an instance of Automobile 
    auto1 = Automobile("Toyota", "Corrola", "12345", "Red", 2005)
    print_data(auto1)

    auto1.set_color("Black")
    
    
    print_data(auto1)
    auto1.honk_horn(4)
    list_of_automobiles = []
    list_of_automobiles.append(auto1)
    list_of_automobiles.append(Automobile("Ferrari", "F-50", "2468", "Red", 2020))
    list_of_automobiles.append(Automobile("Tesla", "Model-S", "98765", "White", 2019))

    print(list_of_automobiles)
    for auto in list_of_automobiles:
        print_data(auto)

    print("Auto Makes and Models")
    for auto in list_of_automobiles:
        print(f"Auto Make: {auto.get_make()}\nModel: {auto.get_model()}\n")
        
            

main()