from collections import Counter
t = int(input())

for _ in range(t):
    w = []
    n = int(input())
    for _ in range(n):
        a,b = input().split()
        w.append(b)
    w_c = Counter(w)
    cnt = 1
    for key in w_c:
        cnt *= w_c[key] + 1
    
    print(cnt-1)
