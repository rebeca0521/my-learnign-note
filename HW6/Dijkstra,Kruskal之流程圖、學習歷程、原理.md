# Dijkstra,Kruskal之流程圖、學習歷程、原理

## 流程圖
### Dijkstra
![](https://i.imgur.com/v98e4C7.jpg)
起點為0，找出0到剩餘每一個vertex的最短路徑。
1. 步驟為先將0納入考慮，(0->0)此時cost為0
2. 接著將觀察其他點是否有與0連接
3. 若有就將點和0的距離填上上圖得下表的第一行，若沒有則填上無限
4. 找出與起點距離最短的vertex(點1)納入可連接的點
5. 再去看與新的可走的點鐘有哪些點跟他連接，或是否會讓距離變短
6. 重錄4.5.步驟直到每個vertax都被納入考慮

上圖最下面一行即為點0到每個點的最短路徑所花費的cost。



---

### Kruskal
![](https://i.imgur.com/Omp7xon.png)
![](https://i.imgur.com/fg43C8D.jpg)
Kruskal會先將Adjacency list做排序，由edge cost最低到高做排序。
步驟 : 
1. 會先畫一個表，將每個點的root初始為-1(也就是root就是自己)
2. 再由cost最小的edge來看是否納入最小路徑
3. 條件為edge的兩個vertex的root不得重複(若重複又納入就會造成cycle)
4. 最後將每個edge都考慮過後就能得出最小cost的路徑


## 學習歷程
### Dijkstra
由Dijkstra原理，可以知道我們需要記得每個vertex的前身(前一個和他連接的vertex)，我稱它為parent，再來我們還需要知道每個vertex和起點的距離distance，最後還要記得已知最短路徑的vertex和尚未知道的vertex。

因此我先寫了以上所需要的東西
```python
from collections import defaultdict 
class Graph(): 

    def __init__(self, vertices): #初始化graph
        self.V = vertices  #vertex個數
        self.graph = []    #matrix
        self.graph_matrix = [[0 for column in range(vertices)]   #沒用到
                    for row in range(vertices)] 

    def Dijkstra(self, s): 
        #尚未找到最小路徑的點的dict
        self.Q = defaultdict(list)       
        for i in range(len(self.graph)) :
            self.Q[i]=self.graph[i]
         
        #每個點的上一個跟他連接的點，初始為-1
        self.pre = defaultdict(list)
        for i in range(vertices):
            self.pre[i].append(-1)
            
        #每個點和起點的最距離
        self.dis = defaultdict(list)
        for i in range(vertices):
            self.dis[i]= 0

```
再來按照我理解的步驟一步一步寫上
```python
    def Dijkstra(self, s): 
        #尚未找到最小路徑的點的dict
        self.Q = defaultdict(list)       #尚未找到最小路徑的list
        for i in range(len(self.graph)) :
            self.Q[i]=self.graph[i]
         
        #每個點的上一個跟他連接的點(初始為-1)
        self.pre = defaultdict(list)
        for i in range(self.V):
            self.pre[i].append(-1)
            
        #每個點和起點的距離(初始為0)
        self.dis = defaultdict(list)
        for i in range(self.V):
            self.dis[i]= 0
        
        #起點的距離為0 
        self.dis[s]=0
        
        #與起點相連接的點和距離    
        for i in self.Q:
            if self.Q[i][s]!= 0 :
                self.pre[i] = s 
                self.dis[i] = self.Q[i][s]
                
        #將起點放到已找到最短路徑的dict
        self.S = []
        self.S.append(s)
            
        #從Q移除已找到的點    
        self.Q.pop(s)

```
上面的部分都是起點所需要的步驟，再來我需要找到和起點的edge cost最小的點，為下一個可走路徑。

因此我另外寫了一個def來處理接下來重複得步驟

```python
from collections import defaultdict 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices #vertex個數
        self.graph = []   #matrix
        self.graph_matrix = [[0 for column in range(vertices)]
                    for row in range(vertices)] 

    def Dijkstra(self, s): 
        #尚未找到最小路徑的點的dict
        self.Q = defaultdict(list)       #尚未找到最小路徑的list
        for i in range(len(self.graph)) :
            self.Q[i]=self.graph[i]
         
        #每個點的上一個跟他連接的點，初始為-1
        self.pre = defaultdict(list)
        for i in range(self.V):
            self.pre[i].append(-1)
            
        #每個點和起點的最距離
        self.dis = defaultdict(list)
        for i in range(self.V):
            self.dis[i]= 0
        
        #起點的距離為0 
        self.dis[s]=0
        
        #與起點相連接的點和距離    
        for i in self.Q:
            if self.Q[i][s]!= 0 :
                self.pre[i] = s
                self.dis[i] = self.Q[i][s]
                #print(i,g.Q[i][s])
                
        #將起點放到已找到最短路進的dict
        self.S = []
        self.S.append(s)
            
        #從Q移除已找到的點    
        self.Q.pop(s)
        
        #dis = self.dis
        return self.BOJIA(self.dis)
    
    def BOJIA(self,dis):
        
        #找到最小的距離當作新的點
        for m in range(len(self.dis)):
            if (self.dis[m]!=0 )&( m not in self.S) :
                min = self.dis[m]
                min_key = m
                break
        for i in range(len(self.dis)):
            if (self.dis[i]!=0) & (self.dis[i] < min)&( i not in self.S):
                min = self.dis[i]
                min_key = i
        #print(min_key,':',min)
        
        #比較比較有和min_key連接的vertex的距離，和他原本的距離哪個比較小，或是是否原本是還沒有距離
        for i in self.Q:
            if i != min_key:
                if self.Q[min_key][i] != 0:
                    if (self.dis[i]==0) | (self.dis[i] > self.Q[min_key][i] + self.dis[min_key]):
                        self.dis[i] = self.Q[min_key][i] + self.dis[min_key]
                        self.pre[i] = min_key
        self.S.append(min_key)
        self.Q.pop(min_key)
        if len(self.Q) != 0:
            self.BOJIA(self.dis)
        return dict(self.dis)

```
最後測試
```python
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],
          [0,0,2,0,0,0,6,7,0]]
g.Dijkstra(0)
```
output : 
```
{0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
```



**最後**
- 雖然我最後沒用到但一開始我不知道這段的意思，所以註記一下
```python
graph_matrix = [[0 for column in range(vertices)]
            for row in range(vertices)] 
            
```
他的意思就是
```python
for row in range(vertices):
    graph_matrix1=[]
    for column in range(vertices):
        graph_matrix1.append(0)
    graph_matrix.append(graph_matrix1)
```
```
vertices = 9
```


output就是
```
[[0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
```




## 原理
### Dijkstra
**最短路徑問題(Shortest Path)** 其中之一的問題為
Single-Source Shortest Path : 從單一vertex，抵達Graph中其餘所有vertex之最短路徑。

而Dijkstra為處理Single-Source Shortest Path的方法。
![](https://i.imgur.com/gg3kPC0.gif)
上圖為Dijkstra Algorithm執行演示（找到A，B之間的最短路），本演算法每次取出未存取節點中距離最小的，用該節點更新其他節點的距離。在演示過程中存取過的節點會被標為紅色。

最壞時間複雜度	O(|E|+|V|\log |V|)

### Kruskal
![](https://i.imgur.com/nGxZaTr.gif)
Kruskal演算法是一種用來尋找最小生成樹的演算法
- 平均時間複雜度 O(|E|\log |V|)
- 最壞空間複雜度	(|E|+|V|)}

### 最小生成樹
最小生成樹其實是最小權重生成樹的簡稱。

一個連通圖可能有多個生成樹。當圖中的邊具有權值時，總會有一個生成樹的邊的權值之和小於或者等於其它生成樹的邊的權值之和。







## Reference
> - http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html
> - http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html
> - https://docs.google.com/presentation/d/e/2PACX-1vTorNDEyhYA4ZAt5jEqOmFs2cQiUAYvkTp-R0DOn9B3c1MuUecV-a1wNakFIrJxA6AoUFGzbl3OQBIJ/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_0
> - https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95
> - https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95
> - https://www.quora.com/What-is-the-difference-between-Dijkstras-Kruskals-and-Prims-algorithms
