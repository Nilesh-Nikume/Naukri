def half_diamond(Hight):
    for i in range(Hight):
        for j in range(i+1):
            print("*", end=' ')
        print()
    for i in range(Hight):
        for j in range(i+1,Hight):
            print("*", end=' ')
        print()
Hight = int(input("Enter Hight of triangle: "))
half_diamond(Hight)
