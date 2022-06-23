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

print("\nMore String Concatination")
character = "*"
print(character * 20)
for number_of_stars in range(10):
    print(character * (number_of_stars + 1))

user_input = input("To continue enter Y")
if user_input.upper() == "Y":
    print("You may continue")
else:
    print("Goodbye")

