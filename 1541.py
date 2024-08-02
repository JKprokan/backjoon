n = input().split("-")
res = []

for i in n:
    sum = 0
    t = i.split("+")
    for j in t:
        sum += int(j)
    res.append(sum)
x= res[0]
for i in range(1,len(res)):
    x -= res[i]
print(x)