def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return num

inputs = []
while True:
    i = int(input())
    if i == 0:
        break
    inputs.append(i)

primes = solution(max(inputs))

for i in inputs:
    for p in primes:
        existance = False
        if p > i // 2:
            break
        if i - p in primes:
            print("{} = {} + {}".format(i, p, i - p))
            existance = True
            break
    if existance == False:
        print("Goldbach's conjecture is wrong.")