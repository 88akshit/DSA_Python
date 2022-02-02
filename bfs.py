# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)


    def printGraph(self):
        print(self.graph)  

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as 
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        level = 0
        #if you want to print all levels start from -1 or 0
        while queue:
            for i in range(len(queue),0,-1):
            # Dequeue a vertex from 
            # queue and print it
              s = queue.pop(0)
              if s==6:
                print('found '+str(s))
                print('level: ',level)
                return
              #print (s, end = " ")

              # Get all adjacent vertices of the
              # dequeued vertex s. If a adjacent
              # has not been visited, then mark it
              # visited and enqueue it
          
              for i in self.graph[s]:
                  
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            
            level+=1
            
        
# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
#g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(2,4)
g.addEdge(3, 3) 
g.addEdge(4, 2) 
g.addEdge(3, 5)
g.addEdge(5, 3)
g.addEdge(3, 6)
g.addEdge(6, 3)
g.printGraph()

print ("Following is Breadth First Traversal"
                  " (starting from vertex )")
g.BFS(0)

someddict = defaultdict(list)
print('s',someddict[3]) # if key not present default empty list would be created
print(someddict)