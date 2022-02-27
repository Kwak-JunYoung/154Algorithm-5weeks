from sys import stdin

n = int(stdin.readline())

a = []

for i in range(n):
    coordinate = stdin.readline().split()
    #coordinate = input().split()

    #map함수 가 더 직관적
    # x, y = stdin.readline().split()

    a.append((int(coordinate[0]), int(coordinate[1])))

#key를 이용하여 x좌표 기준으로 정렬
a = sorted(a, key=lambda pos: (pos[0], pos[1]))

for i in range(n):
    print(a[i][0], a[i][1])