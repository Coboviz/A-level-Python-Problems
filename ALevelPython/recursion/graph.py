numberOfNodes = int(input())
numberOfEdges = int(input())

graph = [[] for _ in range (numberOfNodes)]

# graph = [[], [], [], [], ...., []]
# number of empty lists is equal to the number of nodes

for i in range (numberOfEdges):
    a = int(input())
    b = int(input())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False for _ in range(numberOfNodes)]
dfsList = []

def dfs(startingNode, graph):
    global visited
    visited[startingNode] = True
    print(startingNode, " ", end = "")
    for neighbour in graph[startingNode]:
        if (visited[neighbour] == False):
            dfs(neighbour, graph)
    
   # 8 8 0 7 0 3 7 1 3 6 1 4 4 2 4 5 5 2

dfs(0, graph)
