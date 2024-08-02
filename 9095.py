n = int(input())

def sol(s):
    if s == 1:
        return 1
    elif s == 2:
        return 2
    elif s == 3:
        return 4
    else:
        return sol(s-1) + sol(s-2) + sol(s-3)
    
for _ in range(n):
    s = int(input())
    print(sol(s))
