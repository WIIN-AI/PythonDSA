# for _i in range(5):
#     for _j in range(5):
#         print("*",end=" ")
#     print()


def patterns_2():
    for _i in range(1, 6):
        for _j in range(_i):
            print("*", end=" ")
        print()  # for the new line


def pattern_1(n):
    for row in range(1, n):
        for col in range(1, n):
            print("*", end=" ")
        print()


def pattern_3(n):
    for row in range(1, n):
        for col in range(1, n):
            print("*", end="")


def pattern_4():
    row = 6
    for i in range(1, row + 1):
        for j in range(row - i + 1):
            print("*", end=" ")
        print()

def pattern_5():
    N =5
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def anti_patter_triangle():
    N = 5
    for i in range(2*N+1):
        if i >N:
            for k in range(2*N-i+1):
                print("* ", end=" ")
            print()
        else:
            for j in range(i+1):
                print("* ", end=" ")
            print()

# anti_patter_triangle ()


def anti_patter_triangle_2():
    N = 5
    for i in range(2*N+1):
        if i > N:
            column = 2 * N - i + 1
        else:
            column = i+1

        space = 2*N - column
        for l in range(space):
            print(" ",end="")

        for k in range(column):
            print("*", end=" ")
        print()


# anti_patter_triangle_2()
N =4
N = N*2
for row in range(1,N) :
    for col in range(1,N):
        valAtIndex = True
        print(valAtIndex, end=" ")
    print()

