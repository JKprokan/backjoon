N , n = map(int,input().split())

card = list(map(int,input().split()))
cor = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s = card[i]+ card[j] + card[k]
            cor.append(s)
            s = 0

cor = list(set(cor))
for h in cor[:]:
    if h > n:
        cor.remove(h)

print(max(cor))
            