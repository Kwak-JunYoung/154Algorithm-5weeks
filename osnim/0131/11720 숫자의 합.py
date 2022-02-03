from sys import stdin

#T = int(stdin.readline().rstrip())
#num = int(stdin.readline().rstrip())  # 피제수

""""
T = int(input())
num = int(input()) #피제수
string = input()
result = 0
for _ in range(T):
    result += int(string.pop())
print(result)
"""

T = int(input())
num = int(input()) #피제수
result = 0
temp = 0;

for i in range(1, T + 1):
    Divider = 10 ** i  # 제수
    temp = num % Divider
    temp = int(temp / 10 **(i-1))
    result += temp
print(result)

#고수





