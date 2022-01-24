import math
n = int(input())
fn = str(math.factorial(n))
for i in reversed(range(len(fn))):
    if fn[i] != '0':
        print(len(fn) - i - 1)
        break
