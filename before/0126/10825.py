n = int(input())

student = []
for _ in range(n):
    name, korean, english, math = input().split()
    korean, english, math = list(map(int, [korean, english, math]))
    student.append([name, korean, english, math])
    
student.sort(key=lambda x: x[0])
student.sort(key=lambda x: x[3], reverse=True)
student.sort(key=lambda x: x[2], reverse=False)
student.sort(key=lambda x: x[1], reverse=True)

for s in student:
    print(s[0])