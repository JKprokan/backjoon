cnl = int(input())
b = int(input())
if b == 0:
    a = []
    a.append(abs(100-cnl))
    a.append(len(str(cnl)))
    print(min(a))
    quit()
b_n = list(map(int,input().split()))
result = abs(cnl - 100)

for channel in range(1000001):
    is_possible = True
    for digit in str(channel):
        if int(digit) in b_n:
            is_possible = False
            break
    if is_possible == True:
        result = min(result, len(str(channel)) + abs(cnl - channel))
print(result)

    #런타임에러 내코드
    # cnl = int(input())
    # list_cnl = list(str(cnl))
    # b = int(input())
    # result = []
    # if b == 0:
    #     print(0)
    #     quit()
    # result.append(abs(100-cnl ))
    # b_n = list(map(int, input().split()))
    # x = 0
    # while True:
    #     x += 1
    #     down_cnl = cnl - x
    #     up_cnl = cnl + x
    #     found_d = False
    #     found_u = False
    #     for i in b_n:
    #         if i in list(map(int,str(down_cnl))):
    #             found_d = True
    #     for i in b_n:
    #         if i in list(map(int,str(up_cnl))):
    #             found_u = True
    #     if found_d == False:
    #         result.append(len(list(map(int,str(down_cnl)))) + x)
    #         break
    #     elif found_u == False:
    #         result.append(len(list(map(int,str(up_cnl)))) + x)
    #         break
    # print(min(result))