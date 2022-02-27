import sys

n = int(input())

a = [0]*(n+1)

for i in range(n):
    a[i] = int(input())

#print(a)

def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

result = quick_sort(a)

for i in range(1, n+1):
    print(result[i])