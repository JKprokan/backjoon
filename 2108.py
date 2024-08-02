from collections import Counter
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
max_arr = max(arr)
min_arr = min(arr)

average = round(sum(arr)/n)
print(average)

median = arr[n//2]
print(median)

count_dict = Counter(arr)
most_common = count_dict.most_common(2)
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print(most_common[1][0])
else:
    print(most_common[0][0])

print(max_arr - min_arr) 