n = int(input())
bitmask = 0
result = []
for _ in range(n):
    s= input().split()
    com = s[0]
    if com == "all":
        bitmask = (1 << 20) - 1
    elif com == "empty":
        bitmask = 0
    else:
        num = int(s[1])
    if com == "add":
        bitmask |= (1 << num)
    elif com == "check":
        if bitmask & (1 << num):
            result.append(1)    
        else:
            result.append(0)
    elif com == "remove":
        bitmask &= ~(1 << num)
    elif com == "toggle":
        bitmask ^= (1 << num)
for i in result:
    print(i)
#print("\n".join(result))
