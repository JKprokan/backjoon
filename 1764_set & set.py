import sys
n,m = map(int, sys.stdin.readline().split())
who_1 = set(input() for _ in range(n))
who_2 = set(input() for _ in range(m))
result = list((who_1 & who_2))
result.sort()
print(len(result))
for k in result:
    print(k)