import sys

num = int(sys.stdin.readline())

num_list = []

for i in range(num):
    a = int(sys.stdin.readline())
    num_list.append(a)

num_list.sort()

for i in num_list:
    print(i)