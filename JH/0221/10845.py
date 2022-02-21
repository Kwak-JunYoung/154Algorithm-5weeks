import sys
from collections import deque

n = int(sys.stdin.readline())

def is_empty(queue):
    return int(not bool(queue)) 

queue = deque()

for _ in range(n):
    order = sys.stdin.readline().strip()
    
    if order.startswith('push'):
        push, x = order.split()
        queue.append(int(x)) 
    elif order == 'pop':
        if is_empty(queue):
            print(-1)
        else:
            v = queue.popleft()
            print(v)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        print(is_empty(queue))
    elif order == "front":
        if is_empty(queue):
            print(-1)
        else:
            print(queue[0])
    elif order == "back":
        if is_empty(queue):
            print(-1)
        else:
            print(queue[-1])

### queue = deque() 선언은 for문 밖에서 하기
### 그렇지 않으면 한번 돌 때마다 초기화됨