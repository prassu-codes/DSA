# MINNOO - Rating 604

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Minimum Number of Ones

Your teacher gave you an assignment — given an integer $N$, construct a binary string $B = b_1b_2b_3\ldots b_N$ of length $N$ such that:

$$ \max(b_i, b_{i+1}) = 1 $$

for  **every**  $i$ from $1$ to $N-1$.

What is the  **minimum number**  of $1$'s such a binary string can contain?

 **Note:**  A binary string is a string consisting of only the digits $0$ and $1$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains a single integer $N$ — the length of binary string you'd like to construct.
### Output Format

For each test case, output on a new line the minimum number of $1$'s required to complete the assignment.

### Constraints
- $1 \leq T \leq 1000$
- $2 \leq N \leq 1000$
### Sample 1:
Input
Output

```
6
6
8
2
3
5
100
```

```
3
4
1
1
2
50
```

### Explanation:

 **Test case $1$:**  One possible binary string is $\texttt{010101}$. This has three $1$'s, and it can be verified that the maximum of any two adjacent characters is $1$.
Achieving this with less than three $1$'s is not possible.

 **Test case $2$:**  One possible binary string is $\texttt{10101010}$. This has four $1$'s, and it can be verified that the maximum of any two adjacent characters is $1$.
Achieving this with less than four $1$'s is not possible.

 **Test case $3$:**  One possible binary string is $\texttt{10}$. This has one $1$, and it can be verified that the maximum of any two adjacent characters is $1$.

 **Test case $4$:**  One possible binary string is $\texttt{010}$. This has one $1$, and it can be verified that the maximum of any two adjacent characters is $1$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T16:46:47.219Z  

```py
t = int(input())
for _ in range(t):
    n=int(input())
    print(n//2)

```

---

[View on CodeChef](https://www.codechef.com/problems/MINNOO)