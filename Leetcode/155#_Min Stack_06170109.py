#!/usr/bin/env python
# coding: utf-8

# In[237]:


class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.min = val
        self.next = next
        
class MinStack:

    def __init__(self,top=None):
        """
        initialize your data structure here.
        """
        self.topN=top
        
    def push(self, x: int) -> None:
        if self.topN is  None:
            self.topN = Node(x,None)
        else:
            min_now = self.topN.min 
            self.topN = Node(x,self.topN) 
            if min_now < x:
                self.topN.min = min_now   ## 等號前後位置交換會有差別
            #問題: 如果我打
            #self.top = Node(x,self.top) 
            #if min_now > x:
                #self.topN.min = x
            ##結果跑出來的值會是top不是最小值
            ##原因:1.if min_now < x不成立 self.topN.min就會是新的top的值
            ##    2.min_now = self.topN.min不會影響真正的self.top.min，因為是min_now被寫入原本top.min的值
            ##    3.如果是用我上述所打的方法，後面還要接else: self.topN.min = min_now 才會改變
    def pop(self):
        if self.topN.val is None:
            return
        else:
            self.topN = self.topN.next
            
    def top(self):
        return self.topN.val
## 在此階段發現self.top若跟此定義名字重複(top)會無法使用，因此改成self.topN
                
    def getMin(self):
        return self.topN.min        


# In[238]:


# 以下測試
stack = MinStack()


# In[239]:


stack.push(1)


# In[240]:


stack.push(-3)


# In[241]:


stack.push(-2)


# In[242]:


stack.getMin()


# In[243]:


stack.pop()


# In[244]:


stack.top()


# In[ ]:




