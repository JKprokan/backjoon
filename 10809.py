from string import ascii_lowercase
#알파벳 리스트
s = input()
x = []
for i in ascii_lowercase:
    if i not in s:
        x.append(-1)
    else:
        x.append(s.index(i))
print(" ".join(map(str,x)))