while True:
    S = input()
    if S == "0":
        break
    elif S == S[::-1]:
        print("yes")
    else:
        print("no")
 
