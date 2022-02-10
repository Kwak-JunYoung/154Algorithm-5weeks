ar = []

# 초기화
for row in range(101):
    ar.append([])
    for col in range(11):
        ar[row].append(0)

for j in range(10):
    ar[1][j] = 1

for i in range(2, 101):
    ar[i][0] = ar[i-1][1];
    for j in range(1,10):
        ar[i][j] = ar[i-1][j-1] + ar[i-1][j+1]   
    
# for i in range(len(ar)): 
#     for j in range(len(ar[i])):
#         print(ar[i][j], end=' ')
#     print()

n = int(input())
sum = 0

for i in range(1, 10):
    sum += ar[n][i]

print(sum%1000000000)