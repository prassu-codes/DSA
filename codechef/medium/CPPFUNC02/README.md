# CPPFUNC02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Functions continued

Listen

In the previous task, did you realize that you had to write the detailed formulae for C and D thrice? This repetition can lead to errors and make the code harder to maintain.

```
C = A *A + 2* A *B + B* B
D = A + B

```

Functions allow you to break down a complex program into smaller, manageable modules.
Each function can represent a specific task or functionality.
Once defined, functions can be reused in different parts of the program or even in different programs, promoting code reuse and saving development time.

Instead of writing the formulae repeatedly, you can define functions to calculate C and D. Here’s the syntax for defining a function in C++:

```
return_type function_name(parameters) {
    // function body
    //...
    return result;
}

```

For this task, implement two functions calculateC and calculateD with the following signatures:

```
int calculateC(int A, int B);
int calculateD(int A, int B);

```

Use these functions in your program to calculate the values of C and D for three sets of input A and B.

### Sample 1:
Input
Output

```
3 5
2 7
4 1
```

```
64
8
81
9
25
5
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T06:45:58.241Z  

```c_cpp
#include <iostream>
using namespace std;
int calculateC(int A, int B) {
    return A * A + 2 * A * B + B * B;
}
int calculateD(int A, int B) {
    return A + B;
}
int main() {
    for (int i = 0; i < 3; i++) {
        int A, B;
        cin >> A >> B;   // Use functions to calculate C and D
        int C = calculateC(A, B);
        int D = calculateD(A, B);
        cout << C << endl;
        cout << D << endl;
    }
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CPPFUNC02)