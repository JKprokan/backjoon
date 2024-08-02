tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)

while True:
    
    dup = set(tup)

    tup_list = list(tup)
    dup_list = list(dup)


    for i in dup_list:
        
        tup_list.remove(i)

    if tup_list == list(set(tup_list)):
        break
    
    tup = tup_list
print(max(tup_list))