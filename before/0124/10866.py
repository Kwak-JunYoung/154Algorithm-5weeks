n = int(input())
stack = []
ans = []
for _ in range(n):
    command = str(input())
    if ' ' in command:
        command, what = command.split()

    if command == 'push_back':
        stack.append(what)
    
    elif command == 'push_front':
        stack.insert(0, what)

    elif command == 'pop_back':
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack.pop())

    elif command == 'pop_front':
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack.pop(0))

    elif command == 'size':
        ans.append(len(stack))

    elif command == 'empty':
        if len(stack) == 0:
            ans.append(1)
        else:
            ans.append(0)
            
    elif command == 'front':
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[0])
    
    elif command == 'back':
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])

for a in ans:
    print(a)