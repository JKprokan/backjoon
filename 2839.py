n = int(input())
arr = []

for i in range(5000):
    for j in range(5000):
        if n == 3*i + 5*j:
            arr.append(i+j)

if len(arr) == 0:
    print(-1)
else:
    print(min(arr))