class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
        
class MyQueue(object):
    def __init__(self,front=None,back=None):
        """
        Initialize your data structure here.
        """
        self.front = front
        self.back = back
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.size == 0:
            self.back = self.front = Node(x)
            self.size +=1
        else:
            temp = self.back
            self.back = Node(x)
            temp.next = self.back
            self.size +=1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size ==0 :
            return
            size -=1
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            self.size -=1
            return temp.val
                    

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.size==0:
            return 
        else:
            return self.front.val

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size >0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()