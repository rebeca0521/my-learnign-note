from collections import defaultdict 
  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list)
        self.visited = [] #已造訪過的
        self.Queue = []   #尚未造訪
        self.visited2 = [] #已造訪過的
        self.stack =[]

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def BFS(self, s): 
        for i in range(len(self.graph[s])) : #range(0,len(self.graph[s]))
            if ((self.graph[s][i] in self.Queue) == False) and ((self.graph[s][i] in self.visited)== False):
                self.Queue.append(self.graph[s][i])
            else :
                continue        
        
        if len(self.visited) != 0: #假如是第一個被造訪的就只加到visited，不用pop Queue的front
            self.Queue.pop(0)
        self.visited.append(s) #把s連接的點加到後，就將s加到visited的list
        if len(self.Queue) !=0 :
            self.BFS(self.Queue[0]) #recursion
        return self.visited
    def DFS(self,s):
        self.visited2.append(s)
        for i in range(len(self.graph[s])):
            if ((self.graph[s][i] in self.visited2)==False) & ((self.graph[s][i] in self.stack)== False):
                self.stack.append(self.graph[s][i])
        
        if len(self.stack)!=0 :
            self.DFS(self.stack.pop())
        return self.visited2
            