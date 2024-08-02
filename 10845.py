n = int(input())
stack = []
output = []

for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "front":
        output.append(stack[0] if stack else -1)
    elif command[0] == "back":
        output.append(stack[-1] if stack else -1)
    elif command[0] == "size":
        output.append(len(stack))
    elif command[0] == "empty":
        output.append(1 if not stack else 0)
    elif command[0] == "pop":
        output.append(stack.pop(0) if stack else -1)

for result in output:
    print(result)