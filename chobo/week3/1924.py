x, y = map(int, input().split())
s = 0

for i in range(1, x):
    if i == 2:
        s = s + 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        s = s + 30
    else:
        s = s + 31
s = (s + y) % 7

d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
if s == 0:
    print(d[0])
elif s == 1:
    print(d[1])
elif s == 2:
    print(d[2])
elif s == 3:
    print(d[3])
elif s == 4:
    print(d[4])
elif s == 5:
    print(d[5])
elif s == 6:
    print(d[6])
