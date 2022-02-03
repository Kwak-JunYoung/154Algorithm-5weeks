from itertools import permutations

def formula(arr):
    length = len(arr)
    ans = 0
    for i in range(length - 1):
        ans += abs(arr[i] - arr[i + 1])
    return ans

n = int(input())
a = list(map(int, input().split()))
a_per = list(permutations(a))

print(max([formula(aa) for aa in a_per]))
