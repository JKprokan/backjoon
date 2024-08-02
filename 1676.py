N = int(input())
n = 1
for i in range(1,N+1):
    n *= i
x = list(str(n))
for j in x[::-1]:
        if "0" not in x:
            print("0")
            break

        elif j != "0":
            print(x[::-1].index(j))
            break