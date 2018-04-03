graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F','G']),
         'D': set(['B']),
         'E': set(['B', 'H']),
         'F': set(['C']),
	 'G': set(['C']),
	 'H': set(['E'])}

def dfs_paths(graph, start, destination, path=None):
   if destination == start:
     yield path + [destination]
   if path is None:
     path = []
   path = path + [start]
   for node in graph[start] - set(path):
     for result in dfs_paths(graph, node, destination, path):
       yield result

#list(dfs_paths(graph,'H','F'))
