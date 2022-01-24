days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
wdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = list(map(int, input().split()))
past = sum(days[:x]) + y - 1
print(wdays[past % 7])