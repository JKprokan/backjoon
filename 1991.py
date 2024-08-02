n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    node,left,right = map(str, input().split())
    graph[i].append(node)
    graph[i].append(left)
    graph[i].append(right)

preorder = []
inorder = []
postorder = []

def tree(node):
    preorder.append(graph[node][0])
    
    if graph[node][1] != '.':
        for i in range(1, n+1):
            if graph[i][0] == graph[node][1]:
                tree(i)
                
    inorder.append(graph[node][0])

    if graph[node][2] != '.':
        for i in range(1, n+1):
            if graph[i][0] == graph[node][2]:
                tree(i)

    postorder.append(graph[node][0])

tree(1)
print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))  