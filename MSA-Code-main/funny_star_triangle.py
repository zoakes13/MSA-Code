character = "*"
space = " "
while True:
    try: 
        how_big = int(input("How big do you want the funny triangle? "))
    except:
        print("Please input a number")
    else:
        break

for number_of_stars in range(1,how_big + 1):
    num_of_spaces = how_big - number_of_stars
    print(f"{space * num_of_spaces}{character * number_of_stars}")
