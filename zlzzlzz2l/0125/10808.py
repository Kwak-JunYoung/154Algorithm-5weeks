alpha = ['a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# 입력값 받기
S = list(input())

# 결과값
result = [0 for _ in range(len(alpha))]

# 입력값만큼 반복
for i in S:
    result[alpha.index(i)] += 1 # alpha와 result의 길이가 같기 때문에 alpha에서의 i의 위치에 result 리스트를 1씩 증가하면 된다.

print(" ".join(map(str, result)))