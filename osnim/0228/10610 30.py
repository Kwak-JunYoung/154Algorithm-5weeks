import sys

num = sys.stdin.readline().rstrip()

def sol():
    if '0' not in num:
        print(-1)
        return

    num_list = list(num)
    num_list.sort(reverse=True)
    #print(num_list)

    SUM = 0

    for i in range(len(num_list)):
        #print(num_list[i])

        # 각 자리수의 합이 3의 배수이면 num은 3의 배수
        SUM += int(num[i])

    if SUM % 3 == 0:
        print("".join(num_list))
        return

    else:
        print(-1)
        return

sol()