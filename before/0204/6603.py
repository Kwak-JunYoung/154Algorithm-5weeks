from itertools import combinations
import sys

while True:
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    k = l[0]
    if l[0] == 0:
        break
    real_list = l[1:]
    ps = list(combinations(real_list, 6))
    for p in ps:
        for component in p:
            print(component, end=' ')
        print()
    print()