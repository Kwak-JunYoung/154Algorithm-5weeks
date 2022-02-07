n = int(input())

ar = []
for _ in range(n):
    age, name = input().split()
    ar.append((int(age), name))

ar.sort(key=lambda x: x[0])

for age, name in ar:
    print(age, name)
