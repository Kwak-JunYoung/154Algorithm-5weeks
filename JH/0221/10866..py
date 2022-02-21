import sys
from collections import deque

n = int(sys.stdin.readline())

deck = deque()

for _ in range(n):
    order = sys.stdin.readline().strip()
    
    if order.startswith('push'):
        push, x = order.split()
        if order.startswith('push_front'):
            deck.appendleft(int(x)) # 주의
        elif order.startswith('push_back'):
            deck.append(int(x)) # 주의
    elif order.startswith('pop'):
        if deck:
            if order == 'pop_front':
                v = deck.popleft()
                print(v)
            else: 
                u = deck.pop()
                print(u)
        else: 
            print(-1)
    elif order == 'size':
        print(len(deck))
    elif order == "empty":
        print( int(not bool(deck)) )
    elif order == "front":
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif order == "back":
        if deck:
            print(deck[-1])
        else: 
            print(-1)

'''
order = list(sys.stdin.readline().split()) 을 하면
order[0] --> 명령어
order[1] --> 정수




'''

''' 다른 사람 코드 ( dict 자료형 사용(key, value))
from collections import deque
import sys


N = int(sys.stdin.readline())

dq = deque()

def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0

def size():
    return len(dq)


for i in range(N):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])

    elif cmd[0] == 'push_back':
        dq.append(cmd[1])

    elif cmd[0] == 'pop_front':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.popleft()
            print(tmp)

    elif cmd[0] == 'pop_back':
        if empty() == 1:
            print("-1")
        else:
            tmp = dq.pop()
            print(tmp)

    elif cmd[0] == 'front':
        if empty() == 1:
            print("-1")
        else:
            print(dq[0])

    elif cmd[0] == 'back':
        if empty() == 1:
            print("-1")
        else:
            print(dq[len(dq)-1])

    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'empty':
        print(empty())
'''
