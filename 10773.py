k = int(input())
arr = []
for _ in range(k):
    s = int(input())
    if s == 0:
        del arr[-1]
    else:
        arr.append(s)
print(sum(arr))  