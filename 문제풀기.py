import numpy as np
n = int(input("n을 입력하시오 :"))
a = np.zeros((n,n))
for i in range(0,n):
    a[i,i]=i+1
print(a)


