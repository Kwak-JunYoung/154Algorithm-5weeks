x = input()
n = list(map(str, sorted(list(map(int, list(x))), reverse=True)))

digit_qualified = (sum(list(map(int, list(x)))) % 3 == 0)
have_zero = '0' in x

if digit_qualified and have_zero:
    print(int(''.join(n)))
else:
    print(-1)