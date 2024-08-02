N = int(input())
members = []
for i in range(N):
    age, name = input().split()
    members.append((int(age), name, i))  # 나이, 이름, 가입한 순서를 튜플에 추가

# 나이를 기준으로 정렬하되, 나이가 같으면 가입한 순서로 정렬
members.sort(key=lambda x: (x[0], x[2]))

for member in members:
    print(member[0], member[1])

