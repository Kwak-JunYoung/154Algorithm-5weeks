ans = []
n = int(input())
for i in range(n):
   formula = list(map(int, input().split())) 
   formula.append(sum(formula))
   ans.append(formula)

for i in range(len(ans)):
    print("Case #{}: {} + {} = {}".format(i+1, ans[i][0], ans[i][1], ans[i][2]))