import sys
n = int(sys.stdin.readline())
a = 2
while True:
    if (n == 1 or n == 2):
        print(n)
        break
    a *= 2
    if (a >= n):
        print((n - (a // 2)) * 2)
        break

# card = [i for i in range(1,n+1)]
# while len(card) != 2:
#     a = card[1]
#     card.append(a)
# print(card[1])