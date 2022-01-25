t = int(input())

for i in range(t):
    a ,b = map(int, input().split())
    print("Case #%d: %d + %d = %d"%(i+1, a, b, a+b))