a, b, c = map(int, input().split())
print(f'{(a + b) % c}\n{((a % c) + (b % c)) % c}\n{(a * b) % c}\n{(((a % c) * (b % c)) % c)}')
