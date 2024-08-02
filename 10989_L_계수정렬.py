import sys
N = int(sys.stdin.readline())
arr = [0]*10000

for i in range(N):
    a = int(sys.stdin.readline())
    arr[a-1] += 1

for j in range(10000):
    if arr[j] != 0:
        for k in range(arr[j]):
            print(j+1)



# 내 풀이였는데 메모리 초과로 실패함 
# import sys
# input = sys.stdin.readline
# N = int(input())
# cor = [int(input()) for _ in range(N)]
# #for i in range(N):
#     print(min(cor))
#     cor.remove(min(cor))
# # or print(*cor , sep = "\n")