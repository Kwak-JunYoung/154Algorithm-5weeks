import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for num in range(10001):
    if num_list[num] != 0:
        for j in range(num_list[num]):
            print(num)