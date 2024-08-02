
while True:
    s = list(map(int,input().split()))
    s.sort()
    a= int(s[0])
    b= int(s[1])
    c= int(s[2])
    if a==0 and b==0 and c==0:
        break
    elif c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")
    
    
