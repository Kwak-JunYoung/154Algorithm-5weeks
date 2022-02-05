ans = []
def hanoi(number, start, past, dest):
    if(number == 1):
        ans.append([start, dest])
    else:
        hanoi(number - 1, start, dest, past)
        ans.append([start, dest])
        hanoi(number - 1, past, start, dest)

hanoi(int(input()), 1, 2, 3)
print(len(ans))
for a in ans:
    print(a[0], a[1])