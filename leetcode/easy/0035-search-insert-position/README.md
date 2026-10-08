# Search Insert Position

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

 

 **Example 1:** 

```
Input: nums = [1,3,5,6], target = 5
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,3,5,6], target = 2
Output: 1

```

 **Example 3:** 

```
Input: nums = [1,3,5,6], target = 7
Output: 4

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.7 MB (beats 96.90%)  
**Submitted:** 2026-10-08T11:56:18.136Z  

```py
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        else: 
            for j in range(1,len(nums)):
                if target<nums[j] and target>nums[j-1]:
                    return j 
                    break 
            return len(nums) if target>nums[-1] else 0


        
```

---

[View on LeetCode](https://leetcode.com/problems/search-insert-position/)