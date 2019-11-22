# BST說明
## 原理&流程圖
![](https://i.imgur.com/sbjLYJw.jpg)

## 學習歷程

首先我先寫了insert和search因為感覺比較好寫
### Insert & Solution


#### 問題
* 不能直接寫current.val因為solution裡面沒有val的屬性
* 必須先指定一個node = TreeNode(val) 才能讓 current = node
* pre current沒記到新的node所以left跟right都還是none
* 原本insert最後的return current最後沒記錄到新的node，所以才會出錯
* 改回正確的return

**此階段終極版本**
```python=
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):

    def insert(self, root, val):
        node = TreeNode(val)
        if root == None : #去掉self
            root = node   #去掉self
            #self.size+=1
        else:
            current = root
            while current != None:
                if val <= current.val :
                    pre = current
                    current = current.left
                else :
                    pre = current
                    current = current.right
            if val <= pre.val:
                pre.left = node
                return pre.left
            else :
                pre.right = node
                return pre.right


        
    def search(self, root, target):
        if root == None : #去掉self
            return
        else :
            
            current = root #去掉self
            #self.pre = current  #新增pre node以便delete使用
            
            while target != current.val:
                
                if target < current.val:
                    #self.pre = current
                    current = current.left
                else :
                    #self.pre = current
                    current = current.right
                if current == None:
                    break
                    return None  ##新增 沒找到就停止
                    
            return current


```


### delete
#### 初版
```python=
    def delete(self, root, target):
        while self.search(root,target) != None:
            current =self.search(root,target) #要刪除的node存進current
            
            #如果右邊有child存在，找右邊最小的descendsnt
            if current.right != None:  
                Successor = current.right #右邊最小當作替換數
                pre = Successor ##用來記錄Successor的parent
                while Successor.left != None:
                    pre = Successor
                    Successor = Successor.left
                if Successor.right != None: ##右邊最小值得right還有一個child
                    if Successor != pre: # 如果要刪除的數的右child就是Successor，p就會=Successor
                        pre.left = Successor.right # Successor的parent會接到Successor的child
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.left = current.left
                else: ##右邊最小值得right沒有一個child
                    if Successor != pre: 
                        pre.left = None # Successor的parent的child原本是Successor要改成None
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.left = current.left
                if current == root:
                    root = Successor
                current.left = None
                current.right = None
                        
             #如果左邊有child存在，找左邊最大的descendsnt           
            elif current.left != None:
                Successor = current.left #左邊最大當作替換數
                pre = Successor ##用來記錄Successor的parent
                while Successor.right != None:
                    pre = Successor
                    Successor = Successor.right
                if Successor.left != None: ##右邊最小值得right還有一個child
                    if Successor != pre: # 如果要刪除的數的右child就是Successor，p就會=Successor
                        pre.right = Successor.left # Successor的parent會接到Successor的child
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.right = current.right
                else: ##右邊最小值得right沒有一個child
                    if Successor != pre: 
                        pre.right = None # Successor的parent的child原本是Successor要改成None
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.right = current.right
                if current == root:
                    root = Successor
                current.left = None
                current.right = None
                        
            #current完全沒有child
            #要刪除current的parent的child
            else:
                if self.pre.left == current:
                    self.pre.left = None
                if self.pre.right == current:
                    self.pre.right = None
                if current == root:
                    root == None
        return root

```
#### 問題
* 刪除的node的parent沒連接到Successor
* 要delete的node右邊子樹的最小值有重複的話，直接把左邊子樹整顆接到右子樹最小值後面

            10
           /  \
          9    12
         / \   / \
        7   9 12  15  
  
  delete 10
  
            12
           /  \
          12    15
         /    
        9   
       / \
      7   9
**此階段最終版**
```python=
    def delete(self, root, target):
        while self.search(root,target) != None:
            current =self.search(root,target) #要刪除的node存進current
            
            #如果右邊有child存在，找右邊最小的descendsnt
            if current.right != None:  
                Successor = current.right #右邊最小當作替換數
                pre = Successor ##用來記錄Successor的parent
                while Successor.left != None:
                    pre = Successor
                    Successor = Successor.left
                ## 新增重複值處理
                if pre.val == Successor.val:
                    Successor.left = current.left
                    self.pre.right = current.right
                    
                elif Successor.right != None: ##右邊最小值得right還有一個child
                    if Successor != pre: # 如果要刪除的數的右child就是Successor，p就會=Successor
                        pre.left = Successor.right # Successor的parent會接到Successor的child
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.left = current.left
                    if self.pre.left == current:  ##刪除的node的parent連接到Successor
                        self.pre.left = Successor
                    if self.pre.right == current:
                        self.pre.right = Successor
                else: ##右邊最小值得right沒有一個child
                    if Successor != pre: 
                        pre.left = None # Successor的parent的child原本是Successor要改成None
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.left = current.left
                    if self.pre.left == current:
                        self.pre.left = Successor
                    if self.pre.right == current:
                        self.pre.right = Successor
                if current == root:
                    root = Successor
                current.left = None
                current.right = None
                        
             #如果左邊有child存在，找左邊最大的descendsnt           
            elif current.left != None:
                Successor = current.left #左邊最大當作替換數
                pre = Successor ##用來記錄Successor的parent
                while Successor.right != None:
                    pre = Successor
                    Successor = Successor.right
                if Successor.left != None: ##右邊最小值得right還有一個child
                    if Successor != pre: # 如果要刪除的數的右child就是Successor，p就會=Successor
                        pre.right = Successor.left # Successor的parent會接到Successor的child
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.right = current.right
                    if self.pre.left == current:
                        self.pre.left = Successor
                    if self.pre.right == current:
                        self.pre.right = Successor
                else: ##右邊最小值得right沒有一個child
                    if Successor != pre: 
                        pre.right = None # Successor的parent的child原本是Successor要改成None
                        Successor.left = current.left #Successor的L跟R會接到要刪除的node的LR
                        Successor.right = current.right
                    else:
                        Successor.right = current.right
                    if self.pre.left == current:
                        self.pre.left = Successor
                    if self.pre.right == current:
                        self.pre.right = Successor
                if current == root:
                    root = Successor
                current.left = None
                current.right = None
                        
            #current完全沒有child
            #要刪除current的parent的child
            else:
                if self.pre.left == current:
                    self.pre.left = None
                if self.pre.right == current:
                    self.pre.right = None
                if current == root:
                    root == None
        return root
```

### modify
##### 初版
想法 : 先delete要改變的值，再insert新的值。
```python=
    def modify(self, root, target, new_val):
        if target != new_val: #如果要修改的值和新增的值不同才進行
            if self.search(root,target)!=None: #確認Tree裡有target值
                self.delete(root,target) #先刪除target
                
                for i in range(self.de_num): #根據原本Tree有幾個target去insert新的node數量
                    self.insert(root,new_val)
                return root

```
#### 問題
* 這樣做可能會導致樹高大於遠本的樹，導致效率不彰。
* 因此最後打算把modify完的整棵樹，先丟到list裡，整理成由小到大排序，再把list最中間的值insert回去，list會被拆成左右兩邊，也都是一直丟子list的中間值insert到樹裡。
* 為了操作上面的方法，我又多寫了三個def
1. 把樹的node丟到list裡的def
```python=
    def Print(self,root):
        if root != None:
            self.list.append(root.val)
            self.Print(root.left)
            self.Print(root.right)

```
2.用quick sort排序list
```python=
    def quick_sort(self,array):
        
        if len(array)>=2: 
            pivot = array[len(array)//2] #指定數列中央的數值為基準點
            mid = [] #創三個新的數列
            left = []
            right = []
            for i in array: #將原數列中的每個數值分到新的數列中
                if i == pivot:
                    mid.append(i)
                elif i < pivot:
                    left.append(i)
                else:
                    right.append(i)
            return self.quick_sort(left) + mid + self.quick_sort(right) #左右邊的數列從新再操作一次上面的步驟直到無法再區分
        #self.array = array
        return array

```
3. 把list的值加到新的樹裡
```python=
    def balance(self,root,list):
        if len(list)==1: ##list=[0]
            self.insert(root,list[0])

        elif len(list) == 2: ##list=[0,1]            
            self.insert(root,list[0])
            self.insert(root,list[1])
        else:
            mid = list[int(len(list)/2)]
            self.insert(root,mid)
            L = list[:int(len(list)/2)]
            R = list[int(len(list)/2+1):]
            self.balance(root,L)
            self.balance(root,R)
        return root

```
**modify最終程式碼**
```python=+
    def modify(self, root, target, new_val):
        if target != new_val: #如果要修改的值和新增的值不同才進行
            if self.search(root,target)!=None: #確認Tree裡有target值
                root=self.delete(root,target) #先刪除target
                for i in range(self.de_num): #根據原本Tree有幾個target去insert新的node數量
                    self.insert(root,new_val)
                #return root
                self.list = []
                self.Print(root)
                list = self.quick_sort(self.list)
                #print(list)
                if len(list)==1: ##list=[0]
                    new_root = TreeNode(list[int(len(list)/2)])

                elif len(list) == 2: ##list=[0,1]
                    new_root = TreeNode(list[0])
                    self.insert(new_root,list[1])
                else:
                    new_root = TreeNode(list[int(len(list)/2)])
                    L = list[:int(len(list)/2)]
                    R = list[int(len(list)/2+1):]
                    self.balance(new_root,L)
                    self.balance(new_root,R)
                return new_root
            else:
                return None
                #self.list=[]
                #self.Print(new_root)
                #return print(list)
                #return new_root

                
                #self.new_root = new_root
                self.balance(new_root,list)
                #return print(self.Print(new_root))
                #return self.new_root

```

## 整體問題
* delete和modify完記得要指定新的root給他，因為在做這兩件事的時候會整理整棵樹，root就會因此改變。
>所以有用到的話就要打成
>root = Solution().delete(root,val)

* self就是Class本身，要謹記如何只用self



## 小結
中間有太多小問題了，完整的說明見 [BST新增、查詢、修改、刪除](https://github.com/rebeca0521/my-learning-note/blob/master/HW3/BST%E6%96%B0%E5%A2%9E%E3%80%81%E6%9F%A5%E8%A9%A2%E3%80%81%E4%BF%AE%E6%94%B9%E3%80%81%E5%88%AA%E9%99%A4.md)。

# Reference
> * 吳政翰同學的觀念指點
> * 我的Linked list code
> * http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
> * https://www.youtube.com/watch?v=7vw2iIdqHlM&feature=emb_title
