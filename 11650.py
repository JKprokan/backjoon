N = int(input())
nlist = []

# 중복된 x 좌표를 저장하는 딕셔너리
x_coords = {}

for _ in range(N):
    x, y = map(int, input().split())
    nlist.append([x, y])

# 중복된 x 좌표 검사 및 정렬
for i in range(N):
    if x_coords.get(nlist[i][0]) is None:
        x_coords[nlist[i][0]] = [nlist[i]]
    else:
        x_coords[nlist[i][0]].append(nlist[i])

# 중복된 x 좌표를 가진 요소들을 y 좌표를 기준으로 정렬
for key in x_coords:
    x_coords[key].sort(key=lambda x: x[1])

# 결과 출력
for key in sorted(x_coords.keys()):
    for k in x_coords[key]:
        print(k[0], k[1])

#내가 짠 시간초과 코드
# import sys
# N = int(sys.stdin.readline())
# nlist = []
# for _ in range(N):
#     x,y = map(int,sys.stdin.readline().split())
#     nlist.append([x,y])
    
# for i in range(N-1):
#     for j in range(i+1,N):
#         if (nlist[i][0] == nlist[j][0]) and (nlist[i][1] > nlist[j][1]):
#             a = nlist[i]
#             nlist[i] = nlist[j]
#             nlist[j] = a
        
# for k in nlist:
#     print(k[0],k[1])
