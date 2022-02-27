from sys import stdin

n = int(stdin.readline())

a = []

for i in range(n):
    #coordinate = stdin.readline().split()

    #map함수 가 더 직관적
    x, y = map(int, stdin.readline().split())

    a.append((x, y))

#key를 이용하여 x좌표 기준으로 정렬
a = sorted(a, key=lambda pos: (pos[1], pos[0]))

for i in range(n):
    print(a[i][0], a[i][1])