while True:
    s = list(input())
    if s == ["."]:
       break
    arr = []
    for i in s:
        if i == "[" or i == "]"or i == "(" or i == ")":
            arr.append(i)
    arr = "".join(arr)
    while "()" in arr or "[]" in arr:
        arr = arr.replace("()", "")
        arr = arr.replace("[]", "")
    if len(arr) == 0:
        print("yes")
    else:
        print("no")