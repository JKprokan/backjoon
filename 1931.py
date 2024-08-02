n = int(input())
time = []
cnt = 0
for i in range(n):
    time.append(list(map(int,input().split())))
time.sort(key = lambda x:x[0])
time.sort(key = lambda x:x[1])
s = time[0]
for j in range(1,n):
    if s[1] <= time[j][0]:
        cnt += 1
        s = time[j]
print(cnt+1)