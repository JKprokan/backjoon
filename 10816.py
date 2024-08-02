from collections import Counter

n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

# card 리스트에서 각 숫자의 개수를 미리 계산
card_count = Counter(card)

# arr 리스트에서 각 숫자의 개수를 조회하여 cor 리스트에 저장
cor = [card_count[a] for a in arr]

print(' '.join(map(str, cor)))


# 시간초과된 내 코드
# n = int(input())
# card = list(map(int,input().split()))
# m = int(input())
# arr = list(map(int,input().split()))
# cor = []
# for i in arr:
#     a = card.count(i)
#     cor.append(a)
# print(' '.join(map(str,cor)))