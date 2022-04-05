N = int(input())
rooms = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for room in rooms:
    if room - B >= 0:
        room = room - B
        ans += 1
        a = room // C
        b = room % C
        if b == 0:
            ans += a
        else:
            ans += a + 1
    else:
        ans += 1

print(ans)
