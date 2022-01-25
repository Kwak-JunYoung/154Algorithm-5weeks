st = list(input())

for i in range(1, len(st)+1):
    print(st[i-1], end="")
    if(i % 10 == 0): 
        print()
    

### 다른 풀이

s = input()
for i in range(0, len(s), 10):
    print(s[i:i+10])