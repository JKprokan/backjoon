S = input().upper()
P = list(set(S))
list_R = []
for i in P:
    a = S.count(i)
    list_R.append(a)
if list_R.count(max(list_R)) > 1:
    print("?")
else:
    index_M = list_R.index(max(list_R))
    print(P[index_M])