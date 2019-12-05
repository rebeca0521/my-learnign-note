class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity  ## self.data = [None,None,None,None,None]

    def add(self, key):
        key = self.MD5(key)
        index = key % self.capacity
        node = ListNode(key)
        if self.data[index] == None:
            self.data[index]= node
            
            return 
        else:
            cur = self.data[index]
            while cur.next!=None:
                if cur.val == key:  #若key一樣就不加入
                    return
                else:
                    cur = cur.next
                    if cur.val == key: #若cur.next的值跟key一樣就不加入
                        return
            cur.next = node
            return
    def remove(self, key):
        key = self.MD5(key)
        index = key % self.capacity
        
        if self.data[index] == None:
            return

        
        if self.data[index].val == key:
            self.data[index] = self.data[index].next
            return
        else:  
            cur = self.data[index]
            while cur.next:
                if cur.next.val == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next
            return 
    def contains(self, key):
        key = self.MD5(key)
        index = key % self.capacity 
        cur = self.data[index]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    def MD5(self,key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = int(h.hexdigest(),16)
        return h
