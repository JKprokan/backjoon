case = int(input())
for _ in range(case):
    k = int(input())
    n = int(input())
    k_1 = k
    k_2 = 0
    s = 0    
    a0 = list(range(1,15))
    while k != 0:
        s = 0
        for i in range(14):
            s += a0[14*k_2 + i]
            a0.append(s)
        k -= 1
        k_2 += 1
    print(a0[14*k_1 + n-1])
    
    

# 3 ) 1 5 15 35 70 126
# 2 ) 1 4 10 20 35 56
# 1 ) 1 3 6  10 15 21
# 0 ) 1 2 3  4  5  6  7 8 9 10 11 12 13 14