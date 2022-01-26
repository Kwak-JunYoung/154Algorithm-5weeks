n = int(input())
min = int(1000000)
max = int(-1000000)

s = list(map(int,input().split()))

for i in range(n):
    if(int(s[i]) > max):
        max = s[i]
    if(int(s[i]) < min):
        min = s[i]

print(min, max)