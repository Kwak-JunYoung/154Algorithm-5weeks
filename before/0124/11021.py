ans = []
n = int(input())
for i in range(n):
   a, b = list(map(int, input().split())) 
   ans.append(a + b)

for i in range(len(ans)):
    print("Case #{}: {}".format(i+1, ans[i]))