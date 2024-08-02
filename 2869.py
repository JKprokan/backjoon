a, b, v = map(int, input().split())

count = round(v/(a-b))
if count * (a-b) == v:
    print(count-1)
else:
    print(count)