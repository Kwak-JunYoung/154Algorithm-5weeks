a, b = list(map(int, input().split()))
m = int(input())

a_ary = list(map(str, input().split()))
length = len(a_ary)
a_dec = 0

for i in range(length):
    a_dec += int(a_ary[-(i + 1)]) * pow(a, i)

ans = ''
while a_dec:
    ans = (' ' + str(a_dec % b)) + ans
    a_dec //= b
print(ans[1:])