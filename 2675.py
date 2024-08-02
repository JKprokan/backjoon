T = int(input())

for _ in range(T):
    R,S = input().split()
    B = ""
    for i in range(len(S)):
        A = str(int(R) * S[i])
        B = B+A
    print(B)
    

