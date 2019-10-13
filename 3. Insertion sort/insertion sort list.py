# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:39:40 2019

@author: Rebeca
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if head is None :  # if head = False 
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next : #如果curr.next是true非0
            if curr.next.val < curr.val: # 直到某数小于其前面的数，进入
                pre = dummy
                while pre.next.val < curr.next.val: #從頭開始查找要插到哪裡
                    pre = pre.next
                temp = curr.next # temp 為要被插入前面的數字
                curr.next = temp.next # 將以排序號的最後一位的next指到temp的下一位
                temp.next = pre.next # 將要排序的數的next改為已排序好比第一個比它大的數字
                pre.next = temp #要被排序的數的前一個比它小的數的next改為要被排序的數
            else:
                cur = cur.next
        return dummy.next
