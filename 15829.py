n = int(input())
code = list(input())
s = 0
for i in range(n):
    s += (ord(code[i])-96) * (31**i)
print(s%1234567891)