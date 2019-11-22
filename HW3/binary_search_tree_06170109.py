#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        #self.pre = None ##(新增記前一項)
class Solution(object):
    
    def insert(self, root, val):
        node = TreeNode(val) #要新增的新node
        if root == None : #如果root不存在
            root = node   #新node就會是root
            return root 
        else:
            current = root #current為一指針
            while current != None: #如果current存在
                if val <= current.val 
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
        if root == None : 
            return
        else :
            
            current = root 
            self.pre = current  #新增pre node以便delete使用
            
            while target != current.val:
                
                if target < current.val:
                    self.pre = current
                    current = current.left
                else :
                    self.pre = current
                    current = current.right
                if current == None:
                    break
                    return None  ##(新增) 沒找到就停止
                    
            return current

    def delete(self, root, target):
        self.de_num = 0  #新增delete次數
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
                if pre.val == Successor.val and pre != Successor:
                    Successor.left = current.left
                    self.pre.right = current.right #self.pre.left = Successor
                    
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
                self.de_num +=1
                
                        
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
                self.de_num +=1
                        
            #current完全沒有child
            #要刪除current的parent的child
            else:
                if self.pre.left == current:
                    self.pre.left = None
                if self.pre.right == current:
                    self.pre.right = None
                if current == root:
                    root = None
                self.de_num +=1
        if self.de_num==0 or root == None: 
            return root
        else:  ##整理樹讓樹高小於等於原本的樹
            self.list = []
            self.Print(root)
            list = self.quick_sort(self.list)
            if len(list)==1: ##list=[0]
                root = TreeNode(list[int(len(list)/2)])

            elif len(list) == 2: ##list=[0,1]
                root = TreeNode(list[0])
                self.insert(new_root,list[1])
            else:
                root = TreeNode(list[int(len(list)/2)])
                L = list[:int(len(list)/2)]
                R = list[int(len(list)/2+1):]
                self.balance(root,L)
                self.balance(root,R)

            return root
            
        
        
    def modify(self, root, target, new_val):
        if target != new_val: #如果要修改的值和新增的值不同才進行
            if self.search(root,target)!=None: #確認Tree裡有target值
                root=self.delete(root,target) #先刪除target
                if root == None:
                    for i in range(self.de_num): #根據原本Tree有幾個target去insert新的node數量
                         root=self.insert(root,new_val)
                else:
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



    # 測試recursive
    def Print(self,root):
        if root != None:
            self.list.append(root.val)
            self.Print(root.left)
            self.Print(root.right)
            
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

