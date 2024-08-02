def fib(n):
    a = [1,0,1]
    b = [0,1,1]
    if n >= 3:
        for i in range(2,n):
            a.append(a[i-1] + a[i])
            b.append(b[i-1] + b[i])
    print(f"{a[n]} {b[n]}")

n = int(input())
for _ in range(n):
    x = int(input())
    fib(x)
   
