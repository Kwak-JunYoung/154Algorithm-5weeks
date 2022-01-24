n = int(input())
stack = []
ans = []
for _ in range(n):
    command = str(input())
    if ' ' in command:
        command, what = command.split()

    if command == 'push':
        stack.append(what)

    elif command == 'pop':
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack.pop())

    elif command == 'size':
        ans.append(len(stack))

    elif command == 'empty':
        if len(stack) == 0:
            ans.append(1)
        else:
            ans.append(0)
            
    elif command == 'top':
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])

for a in ans:
    print(a)