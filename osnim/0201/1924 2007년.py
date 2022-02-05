from sys import stdin

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#M, N = map(int, stdin.readline().split())

M, N = map(int, input().split())

days = 0

for i in range(M):
    days += month[i]

print(week[(days+N) % 7])