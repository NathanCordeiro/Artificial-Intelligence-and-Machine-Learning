########################################################
#                                                      # 
#                   EXPERIMENT 1                       # 
#               Breadth First Search                   # 
#              Nathan Cordeiro 22co09                  #
#                                                      #
########################################################

graph={
'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[],
      }
start=input("enter start node:")
def bfs_connected_component(graph):
    visited=[]
    queue=[start]
    while queue:
      node=queue.pop(0)
      if node not in visited:
        visited.append(node)
        neighbours=graph[node]
        for neighbour in neighbours:
          queue.append(neighbour)
    return visited
print("\nHere's the node of the graph by breadth firstsearch",bfs_connected_component(graph))