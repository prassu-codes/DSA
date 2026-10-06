# Perfect Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A  **perfect number**  is a  **positive integer**  that is equal to the sum of its  **positive divisors**, excluding the number itself. A  **divisor**  of an integer `x` is an integer that can divide `x` evenly.

Given an integer `n`, return `true` *if* `n` *is a perfect number, otherwise return* `false`.

 

 **Example 1:** 

```
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

```

 **Example 2:** 

```
Input: num = 7
Output: false

```

 

 **Constraints:** 

- 1 <= num <= 108

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-10-06T12:00:47.610Z  

```py
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        s=1
        p=2
        while p*p<=num:
            if num%p==0:
                s+=p 
                if p!=num//p:
                    s+=num//p 
            p+=1 
        return s==num
```

---

[View on LeetCode](https://leetcode.com/problems/perfect-number/)