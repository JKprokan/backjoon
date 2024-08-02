count = int(input())
pb_con = []
for i in range(count):
    H, W ,N = map(int,(input().split()))
    floor = N%H
    room = N//H
    if floor == 0:
        floor = H
        room = room - 1
    pb_con.append(floor*100 + room + 1)

for j in range(count):
    print(pb_con[j])
