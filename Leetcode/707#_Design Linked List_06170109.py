class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class MyLinkedList(object):

    def __init__(self, head = None):
        self.head = head
        self.size=0
        '''
        加入size方便後續使用
        '''
        
    def get(self, index):
        cur = 0
        cur_node = self.head
        #nexxt_node = cur_node.next
        while cur_node != None:
            if index == cur :
                node = cur_node
                return node.data
            cur += 1 
            cur_node=cur_node.next
            #cur_node = nexxt_node    
        return -1
        '''
        1. 這個問題是python比較討厭的地方。
        2. 從index=2開始就，cur_node一直都沒有呼叫到迴圈外的nexxt_node，
           妳會發現get(2)開始都跟get(1)的值完全一樣。
        3. 因為妳的呼叫方式太過間接了，cur_node = nexxt_node=cur_node.next有三層，
           最多只能用兩層cur_node = cur_node.next。
        '''
        
    def addAtHead(self,data):
        if data is None:
            return None
        node = Node(data,self.head)
        self.head = node
        self.size+=1
        return node
        '''
        有加減東西最後size要記得更動
        '''
    
    def addAtTail(self,data):
        if data is None:
            return None
        
        node = Node(data)
        if self.head is None:
            self.head = node
            self.size+=1
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        self.size+=1
        return node
        '''
        有加減東西最後size要記得更動
        '''
        
    def addAtIndex(self, index: int, data: int):
        
        if index <= 0:
            self.addAtHead(data)
            return

        elif index <= self.size:
            i=0
            curNode=self.head
            pre=curNode
            while True:
                if i == index:
                    pre.next=Node(data,curNode)
                    self.size+=1
                    return
                pre=curNode
                curNode=curNode.next
                i+=1
        '''
        有加減東西最後size要記得更動
        '''
    '''
    def addAtIndex(self, index, data):
        if index<=0:
            self.addAtHead(data)
            return 
        cc = 1
        cur_node = self.head
        n_node = cur_node.next 
        while n_node != None:
            if index == cc:
                node = Node(data,n_node.next)
                n_node = node
                return node
            cc += 1 
            cur_node = n_node
        if index == cc+1:
            node = n_node(data)
            return node
        else:
            return None
    '''  
    def deleteAtIndex(self, index: int):
        if index < 0:
            return 
        
        elif index==0:
            if self.head==None:
                return
            tmp=self.head
            self.head=self.head.next
            tmp.next=None
            self.size-=1
            
        elif index < self.size:
            i=0
            curNode=self.head
            pre=curNode
            while curNode is not None:
                if index==i:
                    pre.next=curNode.next
                    curNode.next=None  #這行看不太懂
                    self.size-=1
                    return
                i+=1
                pre=curNode
                curNode=curNode.next  
    '''
    有加減東西最後size要記得更動
    '''
    
    '''
    def deleteAtIndex(self, index) :
        if index<0:
            return None
        cc = 0
        cur_node = self.head
        n_node = cur_node.next 
        while cur_node != None:
            if index == cc:
                n_node = cur_node
            cc += 1 
            cur_node = cur_node.next
            cur_node = n_node
        return None
    '''
    
    def printList(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    '''
    def printList(self,node):
        node = self.head
        while node:
            print(node)
            node = node.next
    '''
            

l=MyLinkedList()
l.addAtHead(1)
l.addAtHead(2)
l.addAtTail(3)
l.addAtTail(4)
l.head.data
l.head.next.data
l.head.next.next.data
l.head.next.next.next.data

l.get(0).data
l.get(1).data
l.get(2).data
l.get(3).data

l.addAtIndex(1,9)
l.get(1).data
l.printList()
l.addAtIndex(5,10)
l.get(5).data
l.printList()
l.addAtIndex(0,11)
l.printList()

l.deleteAtIndex(0)
l.printList()
l.deleteAtIndex(5)
l.printList()
l.deleteAtIndex(3)
l.printList()






            