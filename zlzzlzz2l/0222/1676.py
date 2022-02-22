def factorial(result, num):
    if num == 0:
        return str(result)
    else:
        result *= num
        return factorial(result, num-1)

N = int(input())
result = 1
cnt = 0
total = factorial(result, N)
for i in range(len(total)-1, 0, -1):
    if total[i] == '0':
        cnt += 1

    if cnt > 0:
        if total[i] != '0':
            break

print(cnt)