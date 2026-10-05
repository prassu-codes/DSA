# CPPFUNC03

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### User defined functions

Listen

User-defined functions are functions that are created by the programmer to perform specific tasks.
These functions are defined by the programmer within the program and are useful for the following reasons

- Code Modularity: Functions allow you to break down a complex program into smaller, manageable parts, making the code easier to understand and maintain.
- Reusability: Once a function is defined, it can be used multiple times throughout the program or even in different programs, saving you from rewriting the same code.
- Readability: Functions with meaningful names provide self-documenting code and improve code readability.

Check the sample syntax below:

```
#include <iostream>
using namespace std;

// User-defined function to calculate the square of a number
int square(int num) {
    return num * num;
}

int main() {
    int num1, num2;
    cin >> num1 >> num2;

    int result1 = square(num1); // Call the square function
    int result2 = square(num2); // Call the square function again

    cout << "Square of " << num1 << " is ", result1 << "\n";
    cout << "Square of " << num2 << " is ", result2 << "\n";

    
}

```

How does the code function?

- The square function is defined to calculate the square of a given number.
- The function is then called twice within the main function to calculate and print the squares of two different numbers.
- This approach eliminates the need to repeat the square calculation logic, making the code more efficient and easier to maintain.
### Task

You need to read 2 user defined input integers - $A$ and $B$.
Print all numbers from 1 to $A$ and 1 to $B$ on separate lines using user defined inputs.
Check sample output below

### Sample 1:
Input
Output

```
5 7
```

```
1 2 3 4 5
1 2 3 4 5 6 7
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T07:38:03.378Z  

```c_cpp
#include <iostream>
using namespace std;
void list_generator(int limit) { 
    for (int i=1;i<=limit;i++){
        cout<<i<<" ";
    }
    cout<<endl;
}
int main() {
    int A, B;
    cin >> A >> B;
    list_generator(A);
    list_generator(B);
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CPPFUNC03)