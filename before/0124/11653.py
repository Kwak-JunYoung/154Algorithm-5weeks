n = int(input())
i = 2
ans = []
while n:
    if n % i == 0:
        ans.append(i)
        n //= i
    else:
        if i <= n-1:
            i += 1
        else:
            break

for a in ans:
    print(a)