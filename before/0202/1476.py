n = int(input())
m = int(input())
buttons = list(map(int, input().split()))

minus = n
plus = n
count = 0

while True:
    if minus == 100 or plus == 100:
        print(count)
        break

    minus -= 1
    plus += 1
    count += 1

    minus_list = list(map(int, str(minus)))
    plus_list = list(map(int, str(minus)))

    minus_incapable = any(element in buttons for element in minus_list)
    plus_incapable = any(element in buttons for element in plus_list)

    if not minus_incapable:
        print(n - minus + len(minus_list))
        break
    elif not plus_incapable:
        print(plus - n + len(plus_list))
        break