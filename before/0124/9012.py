t = int(input())
ans = []
for _ in range(t):
    stack = []
    test = str(input())
    legit = True
    for letter in test:
        if letter == '(':
            stack.append(letter)
        else:
            if stack[-1:] == ['('] and len(stack) != 0:
                stack.pop()
            else:
                legit = False

    if len(stack) == 0 and legit:
        ans.append("YES")
    else:
        ans.append("NO")

for a in ans:
    print(a)