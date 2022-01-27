t = int(input())

for i in range(t):
    a,b= map(int, input().split())
    print("Case #"+str(i+1) +": "+str(a+b))

### "Case #%d: #d"%(i+1,a+b)