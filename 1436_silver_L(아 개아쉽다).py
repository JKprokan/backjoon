N = int(input())
col = 666
count = 0

while True:
    if '666' in str(col):
        count += 1
    if count == N:
        print(col)
        break
    col += 1