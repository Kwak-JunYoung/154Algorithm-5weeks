import sys

num = list(map(int, sys.stdin.readline().rstrip()))

if sum(num)%3 == 0 and 0 in num:
   num.sort(reverse=True)
   print(''.join(map(str, num)))

else:
    print(-1)