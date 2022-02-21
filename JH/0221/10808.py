s = input()

dict_count = { 'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0,'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}


for i in s:
    dict_count[i] += 1

for v in dict_count.values():
    print(v, end=' ')

'''다른 사람 풀이 (아스키 코드)
alpha = [0 for _ in range(26)] 
text = input()

for i in text: 
    alpha[ord(i)-ord('a')]+=1 

### 1, 2번 중에 하나
print(*alpha) # 1번
for n in alpha: # 2번
    print(n, end=" ")
'''
