a,b = map(int,input().split())
y1= 1
y2 = 1
j = 1
k = 2
cor = []
for h in range(1,min(a,b)+1):
    if min(a,b) % h == 0:
        cor.append(h)
for i in cor:
    if max(a,b) % i == 0:
        x = i 
print(x)

while j != k:
    j = max(a,b)*y1
    while k!= j:
        k = min(a,b)*y2
        if k == j:
            print(k)
            break
        elif k > j:
            break
        y2 += 1
    y1 += 1
