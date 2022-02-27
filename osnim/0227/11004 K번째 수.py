import sys

N, K = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

array.sort()

print(array[K-1])