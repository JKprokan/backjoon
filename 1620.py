n, m = map(int, input().split())
arr = {}
re_arr = {}
result = []

for i in range(1, n + 1):
    s_n = input().strip()
    arr[i] = s_n
    re_arr[s_n] = i

for _ in range(m):
    s_m = input().strip()
    if s_m.isdigit():
        result.append(arr[int(s_m)])
    else:
        result.append(str(re_arr[s_m]))

print('\n'.join(result))
#숫자 판별 int변환가능한지, 숫자형태이면, 숫자값표현에 해당되면 True
#isdecimal( ) ⊆ isdigit( ) ⊆ isnumeric( )

#문자열 판별 (알파벳)
#isalpha()

#숫자+알파벳 판별
#isalnum()