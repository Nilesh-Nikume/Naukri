def print_box_Pattern(row, colum):
    for i in range(row):
        for j in range(colum):
            if i == 0 or i == row - 1 or j == 0 or j == colum - 1:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()

row = 3
colum = 3
print_box_Pattern(row, colum)


