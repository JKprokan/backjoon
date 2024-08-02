import sys
N = int(sys.stdin.readline())
pro = []

for _ in range(N):
    pro.append(sys.stdin.readline().strip())

x = list(set(pro))
x.sort()
x.sort(key=len)
for i in x:
    print(i)

