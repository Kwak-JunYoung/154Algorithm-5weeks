#국영수

n = int(input())

stud = []

for _ in range(n):
    name, kor, eng, math = input().split()
    stud.append((name, int(kor), int(eng), int(math)))

stud.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(stud[i][0])

# for i in arr:
#   print(i[0])