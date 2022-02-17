member = []

for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    member.append([age, name])

member.sort(key = lambda member_list: member_list[0])

for m in member:
    print(m[0], m[1])