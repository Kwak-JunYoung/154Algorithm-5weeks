import sys

N, M = map(int, input().split())
input = sys.stdin.readline

list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
list_C = list_A + list_B

for i in sorted(list_C):
    print(i, end=" ")