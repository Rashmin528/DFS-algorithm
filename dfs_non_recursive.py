def dfs_iterative(graph, start):
    stack = [start] #start
    path = [] #empty

    while stack: #stack is not empty
        vertex = stack.pop() #get first node to vertex 
        if vertex in path: #node already in path
            continue #skip
        path.append(vertex) #start adding node to path
        for neighbor in graph[vertex]: #start exploring other node
            stack.append(neighbor) #add neighbor node to stack

    return path


adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

print(dfs_iterative(adjacency_matrix, 1))

#python3 dfs_non_recursive.py