n = int(input())
d = [0] * 12

d[1] = 1
d[2] = 2
d[3] = 4

def sol(x):
    if x <= 3:
        return d[x]
    else: 
        d[x] = sol(x-1) + sol(x-2) + sol(x-3)
        return d[x]

for _ in range(1, n+1):
    print(sol(int(input())))


### 개선

d = [0, 1, 2, 4]
for i in range(4,12):
    d.append(d[i-1]+d[i-2]+d[i-3])

### 개선

for i in range(4, 12):
    d[i] = d[i-1]+ d[i-2] + d[i-3]

for _ in range(n):
    x = int(input())
    print(d[x])

