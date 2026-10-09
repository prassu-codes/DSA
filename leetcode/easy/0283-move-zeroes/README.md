# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.1 MB  
**Submitted:** 2026-10-09T12:05:10.577Z  

```py
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums)==2:
            nums[0],nums[1]==nums[1],nums[0]
        else:   
            for i in range(1,len(nums)-1):
                if nums[i-1]==0 and nums[i]!=0:
                    nums[i],nums[i-1]=nums[i-1],nums[i]
                else:
                    nums[i],nums[i+1]=nums[i+1],nums[i] 
                    nums[i],nums[i-1]=nums[i-1],nums[i]
                



        
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)