n = int(input())
for _ in range(n):
    x = input()
    
    while "()" in x:
        x = x.replace("()", "")
    if len(x) == 0:
        print("YES")
    else:
        print("NO")
    
        
        