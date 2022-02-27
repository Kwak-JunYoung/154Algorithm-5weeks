import sys

n = int(sys.stdin.readline().rstrip())

a = [0]*(10001)
temp = 0

for i in range(n):
    num = int(sys.stdin.readline().rstrip())

    a[num] += 1

# 내장 sort함수가 아닌 계수정렬이용하기
#a.sort()

for i in range(10001):
    # sys.stdout.write(str(a[i])+"\n")
    if a[i] != 0:
        for j in range(a[i]):
            sys.stdout.write(str(i)+"\n")



