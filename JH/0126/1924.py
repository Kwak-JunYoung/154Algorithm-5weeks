x ,y = map(int, input().split())

week = ['SUN','MON','TUE','WED','THU','FRI','SAT']

amon = [1,3,5,7,8,10,12]
bmon = [4,6,9,11]

sum = 0

for i in range(1,x):
    if(i in amon):
        sum += 31
    elif(i in bmon):
        sum += 30
    elif(i ==2 ):
        sum += 28

print(week[(sum + y)%7])
