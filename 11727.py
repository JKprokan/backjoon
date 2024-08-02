n = int(input())
c = [0]*1001
c[1] = 1
c[2] = 3
for i in range(3,1001):
    c[i] = (c[i-1] + 2*c[i-2])%10007
print(c[n])