N = input()
a = 0
N_s = N.split(" ")
N_s = map(int,N_s)

for i in N_s:
    a = a + i**2
print(a%10)

#list를 spr로 붙이기 = join함수
#str을 list로 만들기 = split함수