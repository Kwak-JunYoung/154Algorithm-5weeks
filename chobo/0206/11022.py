n = int(input())
op1 = []
op2 = []
rst = []
for _ in range(n):
    a, b = map(int, input().split())
    op1.append(a)
    op2.append(b)
    rst.append(a + b)

for i in range(len(rst)):
    print("Case #" + str(i+1) + ": " +
          str(op1[i]) + " + " + str(op2[i]) + " = " + str(rst[i]))
