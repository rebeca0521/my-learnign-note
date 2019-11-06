#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def merge_sort(self, nums):
        size = 1
        L=0
        R=1
        newarr=[]
        R_plus_num = 0
        L_plus_num = 0
        while size<len(nums):
            while R<len(nums):
                for i in range(size*2):
                    if nums[L]>nums[R]:
                        newarr.append(nums[R])
                        R+=1
                        R_plus_num+=1
                    else:
                        newarr.append(nums[L])
                        L+=1
                        L_plus_num+=1
                    
                    if R_plus_num >= size:
                        newarr.extend(nums[L:(L+size-L_plus_num)])
                        break
                    if L_plus_num >= size:
                        newarr.extend(nums[R:(R+size-R_plus_num)])
                        break
                    if R>=len(nums):
                        newarr.extend(nums[L:(L+size-L_plus_num)])
                        break
                L = L+size*2-L_plus_num
                R = R+size*2-R_plus_num
                L_plus_num=0
                R_plus_num=0
            if L <len(nums):
                newarr.extend(nums[L:len(nums)])
            nums = newarr
            newarr=[]
            size*=2
            L = 0
            R = size
        return nums
 

