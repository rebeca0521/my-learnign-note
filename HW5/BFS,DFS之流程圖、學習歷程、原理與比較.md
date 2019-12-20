
# BFS,DFS之流程圖、學習歷程、原理與比較
## 流程圖
### BFS
![](https://i.imgur.com/GuR163k.jpg)
由A點開始造訪，A相鄰的BCD會被加到Queue裡，再從Queue的front開始造訪，此時front為B，B相鄰的點為A、E，但A已被造訪過，所以只把E放到Queue的back，後B被pop出Queue，再一次從Queue的front造訪，把相鄰點加到Queue，最後pop...依此類推。最後得到的結果為ABCDEFGHI。

### DFS
![](https://i.imgur.com/UzeQJEa.jpg)
由A開始造訪，相鄰的點有BD，加到stack裡，再由stack的back點D開始造訪(D被pop出stack)，相鄰的點為F，加到stack，又再由stack的back(F點)造訪，F點被移出，相鄰的點A已經被造訪過，所以換stack目前的back(B點)被造訪，B點pop出satck，相鄰的點加入stack...依此類推。最後結果為ADFBCGE。


## 程式碼學習歷程

### BFS
原先不太清楚defaultdict怎麼使用就上網查了一下
>通常在我們取用調用某個dict的key值的時候，都必須事先檢查這個key值是否存在，否則如果直接調用不存在的key值，會直接拋出一個KeyError，collections提供的defaultdict給我們一個很好的解決方案，defaultdict對於我們調用一個不存在的key值，他會先建立一個default值給我們，而這個default值必須由一個可呼叫的函數產生，在我們初始化一個defaultdict時，必須先指定一個產生default值的函數:

```python=
from collections import defaultdict

better_dict = defaultdict(list) # default值以一個list()方法產生
check_default = better_dict['a']
print(check_default) # 會輸出list()方法產生的空串列[]

better_dict['b'].append(1) # [1] 
better_dict['b'].append(2) # [1,2] 
better_dict['b'].append(3) # [1,2,3] 
print(better_dict['b'])
```
##### output為
[]

[1, 2, 3]

了解如何使用defaultdict後就正式開始BFS的了!

首先，我先把我最初的想法寫在紙上
![](https://i.imgur.com/S3DAeSy.jpg)
寫完之後打上jupyter發現這樣的想法會有一點小問題:
* 沒有pop
* 若有pop也要注意第一個被造訪的值會不在Queue裡
因此我稍微做一點修改
```python=
from collections import defaultdict 

class Graph:

    def __init__(self): 
        self.graph = defaultdict(list)
        self.visited = [] #已造訪過的
        self.Queue = []   #尚未造訪


    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def BFS(self, s): 
        for i in range(len(self.graph[s])-1) :
            if (self.graph[s][i] in self.Queue) == False & (self.graph[s][i] in self.visited)== False:
                self.Queue.append(self.graph[s][i])
            else :
                continue        
        
        if len(self.visited) != 0: #假如是第一個被造訪的就只加到visited，不用pop Queue的front
            self.Queue.pop(0)
        self.visited.append(s) #把s連接的點加到後，就將s加到visited的list
        if len(self.Queue) !=0 :
            self.BFS(self.Queue[0])
        else:
            return self.visited
            
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.BFS(2)

```
發現range會有錯誤

而且這樣寫因為遞迴的關係，最後return的會是空值

因此我再修改了一點點
```python=
from collections import defaultdict 
  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list)
        self.visited = [] #已造訪過的
        self.Queue = []   #尚未造訪

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


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.BFS(2))
```
output

[2, 0, 3, 1]

測試文字部分
```python=
g2 = Graph()
g2.addEdge('A','B')
g2.addEdge('A','D')
g2.addEdge('B','C')
g2.addEdge('B','F')
g2.addEdge('C','E')
g2.addEdge('C','G')
g2.addEdge('G','E')
g2.addEdge('E','B')
g2.addEdge('E','F')
g2.addEdge('F','A')
g2.addEdge('D','F')
print(g2.BFS('A'))

```
output

['A', 'B', 'D', 'C', 'F', 'E', 'G']

**完成!!!**:v::smile::v:



### DFS

因為BFS基本觀念差不多都懂了，DFS就好寫很多，所以我就邊畫圖試著照著圖上的步驟打出程式碼，結果沒兩下就打完了!
```python=
    def DFS(self,s):
        self.visited.append(s)
        for i in range(len(self.graph[s])):
            if ((self.graph[s][i] in self.visited)==False) & ((self.graph[s][i] in self.stack)== False):
                self.stack.append(self.graph[s][i])
        
        if len(self.stack)!=0 :
            self.DFS(self.stack.pop())
        return self.visited

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.DFS(2))
```
output

[2, 3, 0, 1]

測試文字部分
```python=
g2 = Graph()
g2.addEdge('A','B')
g2.addEdge('A','D')
g2.addEdge('B','C')
g2.addEdge('B','F')
g2.addEdge('C','E')
g2.addEdge('C','G')
g2.addEdge('G','E')
g2.addEdge('E','B')
g2.addEdge('E','F')
g2.addEdge('F','A')
g2.addEdge('D','F')
print(g2.DFS('A'))

```
output

['A', 'D', 'F', 'B', 'C', 'G', 'E']


## 原理

### BFS
Breadth-first Search（BFS）廣度優先搜尋，是一種圖形(graph)搜索演算法。從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。
廣度優先搜尋法屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理。
![](https://i.imgur.com/lfF2DWi.gif)


### DFS
Depth-first search (DFS) 深度優先搜尋法，是一種用來遍尋一個樹(tree)或圖(graph)的演算法。由樹的root(或圖的某一點當成root)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目 的節點或遍尋全部節點。
深度優先搜尋法屬於盲目搜索(uninformed search)是利用堆疊(Stack)來處理，通常以遞迴的方式呈現。
![](https://i.imgur.com/8UUhoJk.gif)





## 比較


| BFS | DFS |
| -------- | -------- |
| 使用Queue儲存vertex     | 使用Stack儲存vertex     |
| 適合在不斷擴大遍歷範圍時找到相對最優解的情况     | 適合目標比較明確，以找到目標為主要目的的情况     |
|**如果按邊的權重尋找**：比如最短路徑之類的問題，首先找到距離起始點權重為1的點，之後找到權重為2的點…以此類推直至選找到最短的距離，這實質上就是BFS的一種變形。|**如果按鄰接點尋找**：比如尋找迷宮，只有一條到達出口的路徑，這樣的話，通過一個結點，在以這個結點為出發點進行類似操作…直至尋找到出口。即通過DFS的方法。|





# Reference
- https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_44
- https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p
- https://ithelp.ithome.com.tw/articles/10193094
- http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
- https://www.programiz.com/dsa/graph-bfs
- http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
- https://blog.csdn.net/qq_30366449/article/details/77917640
