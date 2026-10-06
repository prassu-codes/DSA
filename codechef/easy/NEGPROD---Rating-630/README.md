# NEGPROD - Rating 630

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Negative Product

Chef is given three numbers $A, B,$ and $C$.

He wants to find whether he can select  **exactly**  two numbers out of these such that the  **product**  of the selected numbers is negative.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three integers $A, B,$ and $C$, the given numbers.
### Output Format

For each test case, output `YES` if Chef can select exactly two numbers out of these such that the product of the selected numbers is negative, `NO` otherwise.

You may print each character in uppercase or lowercase. For example, the strings `NO`, `no`, `No`, and `nO`, are all considered identical.

### Constraints
- $1 \leq T \leq 1000$
- $-10 \leq A, B, C \leq 10$
### Sample 1:
Input
Output

```
5
1 5 7
-5 0 4
6 -1 0
-3 -5 -2
0 0 -4

```

```
NO
YES
YES
NO
NO

```

### Explanation:

 **Test case $1$:**  There exists no way to select two numbers such that their product is negative.

 **Test case $2$:**  The product of $-5$ and $4$ is $-5\cdot 4 = -20$ which is negative.

 **Test case $3$:**  The product of $6$ and $-1$ is $6\cdot (-1) = -6$ which is negative.

 **Test case $4$:**  There exists no way to select two numbers such that their product is negative.

 **Test case $5$:**  There exists no way to select two numbers such that their product is negative.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T05:43:56.499Z  

```py
t = int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    d=0
    for i in a:
        if i<0:
            d+=1
    if a.count(0)>=2 or d>2 or d==0:
        print("no")
    else:
        print("yes")
    
        
   
```

---

[View on CodeChef](https://www.codechef.com/problems/NEGPROD)