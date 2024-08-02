n,k  = map(int, input().split())
s = 1
c = 1
for i in range(k):
    s = s * (n-i)
    c = c * (i+1) 
cor = int(s/c)
print(cor)
