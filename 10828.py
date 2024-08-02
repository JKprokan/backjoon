n = int(input())
stack = []
output = []

for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "top":
        output.append(stack[-1] if stack else -1)
    elif command[0] == "size":
        output.append(len(stack))
    elif command[0] == "empty":
        output.append(1 if not stack else 0)
    elif command[0] == "pop":
        output.append(stack.pop() if stack else -1)

for result in output:
    print(result)

# 내 시간초과된 코드
# n = int(input())
# arr = []
# for _ in range(n):
#     x = input()
#     a = x.split()
#     if "push" in x:
#         arr.append(a[-1])
#     elif x == "top":
#         if len(arr) == 0:
#             print(-1)
#             continue
#         print(arr[-1])
#     elif x == "size":
#         print(len(arr))
#     elif x == "empty":
#         if len(arr) == 0:
#             print(1)
#         else:
#             print(0)
#     elif x == "pop":
#         if len(arr) == 0:
#             print(-1)
#             continue
#         print(arr[-1])
#         arr.pop(-1)
        
