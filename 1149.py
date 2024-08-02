import sys

n = int(input())
house = []
cnt = 0

for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    house.append(s)
d = []
for i in range(1,n):
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]
print(min(house[n-1]))
