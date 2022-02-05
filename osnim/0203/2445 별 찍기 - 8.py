N = int(input())

for i in range(1, N+1):
    print("*"*i + " "*(2*N-2*i) + "*"*i)

for i in range(1, N):
    print("*" *(N-i) + " " * (2 * i) + "*" *(N-i))