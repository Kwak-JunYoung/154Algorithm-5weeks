def factorial(result, num):
    if num == 0:
        return result
    else:
        result *= num
        return factorial(result, num-1)

N = int(input())
result = 1
print(factorial(result, N))