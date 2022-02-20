# i 1 <= n <= 100
# o print star

# n = 5, fixed
#          i
# (0, j = n) ' '=0 * = 5
# (1, ) ' '=1 * = 4
# (2, ) ' '=2 * = 3
# (3, ) ' '=3 * = 2
# (4, ) ' '=4 8 = 1

# 1,0
# 2,0 2,1
# 3,0 3,1 3,2
n = int(input())
for i in range(n):
    for j in range(n):
        if (j < i):
            print(" ", end="")
        else:
            print("*", end="")
    print()
