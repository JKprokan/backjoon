from collections import deque
n,k= map(int,input().split())
arr = deque([i for i in range(1,n+1)])
cor = []
while len(arr) != 0:
    for _ in range(k-1):
        arr.append(arr.popleft())
    cor.append(str(arr.popleft()))
print('<'+', '.join(cor)+'>')
