n = int(input())
c = [0]*1001
c[1] = 1
c[2] = 2
for i in range(3,1001):
    c[i] = (c[i-1] + c[i-2])%10007
print(c[n])

# 정답인 내 코드이지만 사실 DP문제였다
# n = int(input())
# def factorial (f):
#     s = 1
#     for i in range(1,f+1):
#         s *= i
#     return s

# def combination (a,b):
#     return factorial(a) // (factorial(b) * factorial(a-b))
# result = 0
# j = 0
# for i in range(n,0,-1):
#     if i < j:
#         break
#     result += combination(i,j)
#     j+=1
# print(result%10007)