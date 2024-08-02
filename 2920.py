a = {1:"c", 2:"d", 3:"e", 4:"f", 5:"g", 6:"a", 7:"b", 8:"C"}
b = []
N = map(int,input().split())

for i in N:
    b.append(a[i])
goal = "".join(b)
if goal == "cdefgabC":
    print("ascending")
elif goal == "Cbagfedc":
    print("descending")
else :
    print("mixed")
    