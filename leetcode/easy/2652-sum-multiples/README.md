# Sum Multiples

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer `n`, find the sum of all integers in the range `[1, n]`  **inclusive**  that are divisible by `3`, `5`, or `7`.

Return  *an integer denoting the sum of all numbers in the given range satisfying the constraint.* 

 

 **Example 1:** 

```
Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.

```

 **Example 2:** 

```
Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.

```

 **Example 3:** 

```
Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.

```

 

 **Constraints:** 

- 1 <= n <= 103

## Solution

**Language:** Python  
**Runtime:** 27 ms (beats 58.86%)  
**Memory:** 19.4 MB (beats 13.76%)  
**Submitted:** 2026-10-05T11:27:34.505Z  

```py
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum+=i  
        return sum     
```

---

[View on LeetCode](https://leetcode.com/problems/sum-multiples/)