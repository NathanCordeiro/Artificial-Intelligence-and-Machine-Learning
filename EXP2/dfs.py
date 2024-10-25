########################################################
#                                                      # 
#                   EXPERIMENT 2                       # 
#                Depth First Search                   # 
#              Nathan Cordeiro 22co09                  #
#                                                      #
########################################################

graph={
'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':[],
'E':[],
'F':[],
'G':[],
}
start=input("enter start node:")
def dfs_traversal(graph):
 visited=[]
 stack=[start]
 while stack:
   node=stack.pop()
   if node not in visited:
     visited.append(node)
     neighbours=graph[node]
   for i in neighbours:
     stack.append(i)
 return visited
print("\nHere's the node of the graph by depth first search:",dfs_traversal(graph))
