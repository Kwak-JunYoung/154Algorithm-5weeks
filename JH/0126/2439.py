n = int(input())

for i in range(n-1, -1, -1):
    print(" "*i + '*'*(n-i), end='') #'+'로 연결해야함 ,로 하면 처음에 공백생김
    print()