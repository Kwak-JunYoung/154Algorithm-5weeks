string = list(input())
result = ""

for i in range(0, len(string)):
    result += string[i]

    if len(result) == 10:
        print(result)
        # print("".join(string))
        result = ""
print(result)
