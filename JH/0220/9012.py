import sys

n = int(sys.stdin.readline())


for _ in range(n):
    stack = []

    ps = sys.stdin.readline().strip()
    ps = list(ps)
    if len(ps) %2 == 1: # 총 개수 홀수면 바로 NO
        print("NO")
    else: 
        for i in range(len(ps)):
            if ps[i] == "(":
                ps[i] = -1
            else: 
                ps[i] = 1
        for x in ps:
            if (not bool(stack)): #stack 비어있으면
                stack.append(int(x))
            else:
                # if(stack[-1] + int(x) == 0):
                if (stack[-1] == -1 and int(x) == 1):
                    stack.pop()
                else:
                    stack.append(int(x))
        if (not bool(stack)): 
            print("YES")
        else:
            print("NO")


### 틀림
'''
1. 답이 틀림
stack을 for문 한번 돌면 비워줘야함 or stack을 for문 안에서 선언
--> 해결

2. 위의 식으로 풀었을 경우의 예외 --> ())(() NO 인데 YES로 출력됨
위의 식은 (), )( 모두 가능하게 푼 방법임
--> 수식 수정 필요


'''