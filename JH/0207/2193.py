n = int(input())

d = [0] * (n+1) #91로 해도됨
d[1] = 1
d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

### n == 1의 경우 d[0, 0] 으로 d[2] 가 없어서 IndexError 난거임

#### 해결
n = int(input())

if n == 1:
    print(1)
else:
    d = [0] * (n+1) 
    d[1] = 1
    d[2] = 1

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    print(d[n])