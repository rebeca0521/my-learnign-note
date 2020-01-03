#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def sortArray(self, nums):    
        if len(nums)>=2:
            i=0
            j=0 
            pivot = nums[len(nums)-1]
            while j != (len(nums)-1):
                if nums[j] >= pivot:
                    j+=1
                else:
                    temp_i = nums[i]
                    temp_j = nums[j]
                    nums[i] = temp_j
                    nums[j] = temp_i
                    i+=1
                    j+=1
            temp_i = nums[i]
            temp_j = nums[j]
            nums[i] = temp_j
            nums[j] = temp_i
            return self.sortArray(nums[:i]) + [pivot] + self.sortArray(nums[(i+1):])
        return nums


# In[3]:


A = Solution()


# In[4]:


A.sortArray([5,8,9,4,1,0,3])


# In[ ]:




