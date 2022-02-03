N = int(input())

for i in range(1, N+1):
    if i == N:
        print("*"*(2*i-1))
    elif i == 1:
        print(" " * (N - i) + "*" + " " * (2 * i - 3))
    else:
        print(" "*(N-i) + "*" +" "*(2*i-3) +"*")
