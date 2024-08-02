h,w = map(int,input().split())
problem = []
count = []
for _ in range(h):
    problem.append(input())

for i in range(h-7):
    for j in range(w-7):
        index1 = 0
        index2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if problem[a][b] != "W":
                        index1 += 1
                    if problem[a][b] != "B":
                        index2 += 1
                else:
                    if problem[a][b] != "B":
                        index1 += 1
                    if problem[a][b] != "W":
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))
    