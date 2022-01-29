alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# 입력값 받기
S = list(input())

# 결과값
result = []

# alpha만큼 반복
for i in alpha:
    if i in S: # i가 S에 속해있다면
        result.append(S.index(i)) # S안에 있는 i의 인덱스를 result에 추가
    else: # 아니라면
        result.append(-1) # -1 추가

print(" ".join(map(str, result)))