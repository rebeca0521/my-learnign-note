#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices #vertex個數
        self.graph = []   #matrix
        self.graph_matrix = [[0 for column in range(vertices)]
                    for row in range(vertices)] 
        

            
    def addEdge(self,u,v,w): 
        pass
    def Dijkstra(self, s): 
        #尚未找到最小路徑的點的dict
        self.Q = defaultdict(list)       #尚未找到最小路徑的list
        for i in range(len(self.graph)) :
            self.Q[str(i)]=self.graph[i]
         
        #每個點的上一個跟他連接的點，初始為-1
        self.pre = defaultdict(list)
        for i in range(self.V):
            self.pre[str(i)].append(-1)
            
        #每個點和起點的最距離
        self.dis = defaultdict(list)
        for i in range(self.V):
            self.dis[str(i)]= 0
        
        #起點的距離為0 
        #self.dis[s]=0
        
        #與起點相連接的點和距離    
        for i in self.Q:
            if self.Q[i][s]!= 0 :
                self.pre[i] = s
                self.dis[i] = self.Q[i][s]
                #print(i,g.Q[i][s])
                
        #將起點放到已找到最短路進的dict
        self.S = []
        self.S.append(str(s))
            
        #從Q移除已找到的點    
        self.Q.pop(str(s))
        
        #dis = self.dis
        return self.BOJIA(self.dis)
    
    def BOJIA(self,dis):
        
        #找到最小的距離當作新的點
        for m in self.dis:
            if (self.dis[m]!=0 )&( m not in self.S) :
                min = self.dis[m]
                min_key = m
                break
        for i in self.dis:
            if (self.dis[i]!=0) & (self.dis[i] < min)&( i not in self.S):
                min = self.dis[i]
                min_key = i
        #print(min_key,':',min)
        
        #比較比較有和min_key連接的vertex的距離，和他原本的距離哪個比較小，或是是否原本是還沒有距離
        for i in self.Q:
            if i != min_key:
                if self.Q[min_key][int(i)] != 0:
                    if (self.dis[i]==0) | (self.dis[i] > self.Q[min_key][int(i)] + self.dis[min_key]):
                        self.dis[i] = self.Q[min_key][int(i)] + self.dis[min_key]
                        self.pre[i] = min_key
        self.S.append(min_key)
        self.Q.pop(min_key)
        if len(self.Q) != 0:
            self.BOJIA(self.dis)
        return dict(self.dis)
    def Kruskal(self):
        pass

