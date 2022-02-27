import sys
n = int(sys.stdin.readline())

#a = []

a={}

for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    if data in a:
        a[data] += 1
    else:
        a[data] = 1

result = sorted(a.items(), key = lambda x:(-x[1], x[0]))
#print(result)
sys.stdout.write(str(result[0][0]))
