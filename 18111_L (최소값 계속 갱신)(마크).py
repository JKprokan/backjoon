import sys
n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
count = 0
for k in range(257):
    max, min = 0, 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] >= k:
                max += ground[i][j] - k
            else:
                min += k - ground[i][j]
    
    if max + b >= min:
        if min + (max * 2) <= answer:
            answer = min + (max * 2)
            count = k
print(answer , count)
#answer로 최소값을 계속 갱신


#2차원리스트 1차원으로 만들기 
# - sum(listname, [])
# - list(itertools.chain(*listname))
