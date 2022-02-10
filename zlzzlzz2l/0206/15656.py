from itertools import product # 중복순열 라이브러리

N, M = map(int, (input().split())) # N과 M 입력 받기

data = sorted(list(map(int, input().split()))) # N개의 수 오름차순 리스트화

result = list(product(data, repeat=M)) # data 리스트 안에서 순서에 상관없이 서로 다른 M개 선택 (중복 가능)

for i in result:
    print(' '.join(map(str, i))) # 튜플 값을 문자열로 바꾼 뒤 문자열로 합친다. 튜플 -> 문자열