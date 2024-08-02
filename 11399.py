n = int(input())
p = list(map(int,input().split()))
p.sort()

s, a = 0, 0
for i in range(n):
    a += p[i]
    s += a
print(s)
