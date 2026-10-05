# DNASTORAGE - Rating 801

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### DNA Storage

For encoding an even-length binary string into a sequence of `A`, `T`, `C`, and `G`, we iterate from  **left to right**  and replace the characters as follows:

- 00 is replaced with A
- 01 is replaced with T
- 10 is replaced with C
- 11 is replaced with G

Given a binary string $S$ of length $N$ ($N$ is even), find the encoded sequence.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- First line contains a single integer $N$, the length of the sequence.
- Second line contains binary string $S$ of length $N$.
### Output Format

For each test case, output in a single line the encoded sequence.

 **Note:**  Output is  **case-sensitive**.

### Constraints
- $1 \leq T \leq 100$
- $2 \leq N \leq 10^3$
- $N$ is even.
- Sum of $N$ over all test cases is at most $10^3$.
- $S$ contains only characters 0 and 1.
### Sample 1:
Input
Output

```
4
2
00
4
0011
6
101010
4
1001

```

```
A
AG
CCC
CT
```

### Explanation:

 **Test case $1$:**  Based on the rules `00` is replaced with `A`.

 **Test case $2$:**  Based on the rules `00` is replaced with `A`. Similarly, `11` is replaced with `G`. Thus, the encoded sequence is `AG`.

 **Test case $3$:**  The first two characters are `10` which is encoded as `C`. Similarly, the next two characters `10` are encoded as `C` and the last two characters `10` are encoded as `C`. Thus, the encoded string is `CCC`.

 **Test case $4$:**  The first two characters are `10` which is encoded as `C`. Similarly, the next two characters `01` are encoded as `T`. Thus, the encoded string is `CT`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T16:13:05.545Z  

```py
t = int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=0
    r=1
    b=""
    while r<=len(s):
        if s[l]=='0' and s[r]=='0':
            b+='A'
        elif s[l]=='0' and s[r]=='1':
            b+='T'
        elif s[l]=='1' and s[r]=='0':
            b+='C'
        else:
            b+='G'
        l+=2
        r+=2
    print(b)
            
        

```

---

[View on CodeChef](https://www.codechef.com/problems/DNASTORAGE)