string = list(input())
print(string)

arr_alpha = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr_index = [-1] * 26

for char in string:
    arr_index[arr_alpha.index(char)] = string.index(char)

for i in arr_index:
    print(i, end=' ')



'''틀왜맞???ㅋㅋㅋㅋㅋㅋㅋㅋ
내가 생각할 때, 같은 알파벳이 뒤에 나오는 경우 그 인덱스로 바뀌는 줄 알았는데 아님....왜???

idea :  최초에 -1일때만 자리값을 넣어주도록 하기

'''

'''다른 사람 코드

word = input()
alph = list(range(97, 123))

for x in alph:
    print(word.find(chr(x)), end=' ')

'''