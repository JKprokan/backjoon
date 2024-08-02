count = int(input())
x,a = 0,1

for i in range(count):
    pb = list(input())
    for j in pb:
        if j == "X":
            a = 1
        else:
            x = x + a
            a += 1
    print(x)
    x,a = 0,1
