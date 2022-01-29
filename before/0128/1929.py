def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return num


a, b = list(map(int, input().split()))

primes = sorted(solution(b))

for prime in primes:
    if prime >= a:
        print(prime)
