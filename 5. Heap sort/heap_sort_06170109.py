#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):  
    def heap_sort(self,nums:list):

        sorted_array=[]
        while len(nums)>=1:
            self.heapify(nums)
            nums[0],nums[-1]=nums[-1],nums[0]
            sorted_array.append(nums[-1])
            nums.pop()
        sorted_array.reverse()
        return sorted_array
        
    def siftdown(self,nums:list,maxindex):
        while maxindex < len(nums):
            premom = maxindex
            L = (premom*2)+1
            R = (premom*2)+2
            if L < len(nums)-1:
                if R<=len(nums)-1:
                    if nums[L]>nums[R]:
                        maxindex = L
                        if nums[maxindex]>nums[premom]:
                            nums[maxindex],nums[premom] = nums[premom],nums[maxindex]
                        else :
                            return
                    else:
                        maxindex = R
                        if nums[maxindex]>nums[premom]:
                            nums[maxindex],nums[premom] = nums[premom],nums[maxindex]
                        else :
                            return
                else:
                    maxindex = L
                    if nums[maxindex]>nums[premom]:
                        nums[maxindex],nums[premom] = nums[premom],nums[maxindex]
                    else :
                        return    
            else:
                return nums
        return nums
    
    def heapify(self,nums:list):
        i = len(nums)-1
        while i>0:
            maxindex = i
            if i%2==0:
                mom = int((i-2)/2)
                i-=1
                if nums[maxindex]>nums[i]:
                    if nums[maxindex]>nums[mom]:
                        nums[maxindex],nums[mom]=nums[mom],nums[maxindex]
                        self.siftdown(nums,maxindex)
                else:
                    maxindex = i
                    if nums[maxindex]>nums[mom]:
                        nums[maxindex],nums[mom]=nums[mom],nums[maxindex]
                        self.siftdown(nums,maxindex)
            else:
                mom = int((i-1)/2)
                i-=1
                if nums[maxindex]>nums[i]:
                    if nums[maxindex]>nums[mom]:
                        nums[maxindex],nums[mom]=nums[mom],nums[maxindex]
                        self.siftdown(nums,maxindex)
                else:
                    maxindex = i
                    if nums[maxindex]>nums[mom]:
                        nums[maxindex],nums[mom]=nums[mom],nums[maxindex]
                        self.siftdown(nums,maxindex)
            i-=1
                
        return nums

