import sys

N = sys.stdin.readline().rstrip()
#length = int(len(N)/2)
left, right = 0, 0

for i in range(len(N)):
    if i < len(N)/2:
        left += int(N[i])
    else:
        right += int(N[i])

if left == right:
    print("LUCKY")
else:
    print("READY")

