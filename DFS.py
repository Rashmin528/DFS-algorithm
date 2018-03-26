graph = {'A': ['B','C'],
         'B': ['A','D','E'],
         'C': ['F','G','A'],
	 'D': ['B'],
	 'E': ['H','B'],
	 'F': ['C'],
	 'G': ['C'],
	 'H': ['E']}

def dfs(graph,start,end,route,list):
    route+=[start]
    if start == end:
        list.extend(route)
    else:
        for node in graph[start]:
            if node not in route:
                dfs(graph,node,end,route,list)

def dfs_route(graph,start,end):
      list = []
      dfs(graph,start,end,[],list)
      return list

print(dfs_route(graph,'A','H'))
