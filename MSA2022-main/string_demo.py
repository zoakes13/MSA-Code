sentence = "The quick brown fox jumps over the lazy dog"

print("\nEndswith")
file_name = "numbers"
if not file_name.endswith(".txt"):
    file_name = file_name + ".txt"
print(file_name)

print("\nString concancelation")
first_name = "Zack"
last_name = "Oakes"
full_name = first_name + " " + last_name
print(full_name)

print("\nString Indexes")
print(full_name[0])
for letter in full_name:
    print(letter)

print("\nString Slicing")

print(full_name[0:5])
#Print from a specified index until the end of the string
print(full_name[7:])
#Reverse a string
print(full_name[::-1])

user_input = input("To continue enter Y")
if user_input.upper() == "Y":
    print("You may continue")
else:
    print("Goodbye")
