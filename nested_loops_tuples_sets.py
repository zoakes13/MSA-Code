nest_list = [[76, 94, 29],
            [55, 43, 98],
            [74, 23, 88]]

for row in nest_list:
    for column_value in row:
        print(column_value)

for row_number in range(len(nest_list)):
    print(f"\nRow {row_number + 1} Values\n-----------------")
    for column_value in range(len(nest_list[row_number])):
        print(f"Column {column_value + 1}: {nest_list[row_number][column_value]}")

print("\nTuple Demo")