import sys
K,N = map(int,input().split())
line = [int(sys.stdin.readline()) for i in range(K)]
start = 1
end = max(line)
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for j in line:
        cnt += j//mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
    
#내 코드 ( 정답은 맞는거 같은데? 근데 시간초과됌)
# K,N = map(int,input().split())
# line = [int(input()) for i in range(K)]
# cor = []
# x=1
# c = 0
# while x != max(line):

#     count ,w ,c = 0,0,0
#     for j in range(K):
#         count = line[j]//x
#         w += count
#     c = w
#     if c == N:
#         cor.append(x)
#     x += 1
# print(cor)