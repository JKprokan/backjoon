N = input()
s = 0
for i in range(int(N)):
    s = 0
    for j in list(str(i)):
        s += int(j)
    if s + i == int(N):
        print(i)
        quit()
print(0)
