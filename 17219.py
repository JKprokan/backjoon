n, m = map(int, input().split())
site = []
passwd = []
result = []
for _ in range(n):
    s = input().split()
    site.append(s[0])
    passwd.append(s[1])

for i in range(m):
    w_site = input()
    a = site.index(w_site)
    result.append(passwd[a])
print("\n".join(result))
