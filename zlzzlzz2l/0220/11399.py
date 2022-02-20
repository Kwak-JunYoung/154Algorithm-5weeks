# 입력값 받기
N = int(input())
person = list(map(int, input().split(" ")))
# 오름차순 정렬
person.sort()

# 기다린 시간 넣어줄 리스트 및 변수
result = [person[0]]
person_result = person[0]

for i in range(1, len(person)):
    person_result += person[i] # 맨 앞 사람부터 누적해서 시간을 더해준다.
    result.append(person_result) # 누적된 시간을 리스트에 넣어준다.

print(sum(result)) # 리스트의 합이 최소 시간

