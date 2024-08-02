n = int(input())
arr = []
for _ in range(n):
    s = int(input())
    arr.append(s)
x = int((n*0.15)+0.5)
arr.sort()
result = arr[x:n-x]

if n == 0:
    print(0)
else:
    print(int(sum(result)/len(result)+0.5))