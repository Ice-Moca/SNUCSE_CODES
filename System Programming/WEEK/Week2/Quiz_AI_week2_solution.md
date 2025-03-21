# 2025 Spring SNU System Programming - Weekly Quiz (Week 2, with Solutions)

We have prepared some light quizzes related to class content of week 2.  
These problems have been selected from those generated by **AI tool (Cramify)**,  
based on your class ppt content.

There is no need to submit anything after reviewing this material,  
but we hope it will help you review the class content you learned this week and prepare for the quiz.

---

Weekly Quiz has two documents, one with only the problems and  
the other with both the problems and solutions.  

# Question 1

Consider the following C code snippet:

```c
#include <stdio.h>

int main(void) {
  int state = 1;
  char input;

  while ((input = getchar()) != EOF) {
    if (state == 1 && input == 'a') {
      // Perform some action
      state = 2;
    } else if (state == 2 && input == 'b') {
      // Perform another action
      state = 1;
    }
  }
  return 0;
}
```

What is the primary advantage of replacing the magic numbers 1 and 2 with named constants like `STATE_A` and `STATE_B` using `enum` or `#define?`

A) Faster execution speed  
B) Reduced memory consumption  
C) Improved code readability and maintainability  
D) Enhanced type safety  

**Answer: C**

**Solution:**  
Magic numbers like 1 and 2, when used to represent states or other meaningful values, reduce code readability and maintainability.  
Replacing them with named constants like `STATE_A` and `STATE_B` makes the code self-documenting, clearly indicating the purpose of these values.  
This improves readability, making it easier to understand the code's logic, and simplifies maintenance by allowing changes to these values in a single location.

# Question 2

Outline the four key stages involved in building a C program, briefly describing the purpose and outcome of each stage.  
Specifically, what transformations occur to the source code at each step, and what are the intermediate file types generated?

**Answer:**  
Preprocessing: Handles preprocessor directives, removes comments, expands macros, and includes header files. Output: modified source code (.i)  
Compiling: Translates preprocessed code into assembly language. Output: assembly language file (.s)  
Assembling: Converts assembly language to machine code. Output: object file (.o)  
Linking: Combines object files and libraries to create an executable. Output: executable file  

**Solution:**  
The four stages of building a C program are:
1. Preprocessing: This stage handles preprocessor directives (e.g., #include, #define). It removes comments, expands macros, and includes header files. The output is a modified source code file (e.g., .i). The source code is still in C language but with all preprocessor directives handled.  
2. Compiling: The compiler translates the preprocessed source code into assembly language specific to the target machine architecture. This stage checks for syntax errors and generates an assembly language file (e.g., .s). The code is now in a lower-level language closer to machine instructions.  
3. Assembling: The assembler converts the assembly language code into machine code, producing an object file (e.g., .o). Object files contain machine instructions but may have unresolved references to external functions or variables. The code is now in machine language but not yet ready to execute.  
4. Linking: The linker combines the object files with necessary libraries (e.g., libc.a) to resolve external references and create an executable file. This stage produces the final executable program that can be run on the target system. The code is now a complete, executable program.

# Question 3

Given the following C code snippet:

```c
#include <stdio.h>

int main(void) {
    printf("characters: %c %c %c\n", 'A' + 'a' - 'A', 'c' - ('a' - 'A'), 'D' + 32);
    return 0;
}
```

What will be the output of this program?

**Answer:**  
characters: a C d

**Solution:**  
1. **'A' + 'a' - 'A'**: This simplifies to 'a'. Thus, the first character printed is 'a'.  
2. **'c' - ('a' - 'A')'**: The difference between 'a' and 'A' represents the offset between lowercase and uppercase letters in ASCII. Subtracting this offset from 'c' effectively converts 'c' to its uppercase equivalent, 'C'.  
3. **'D' + 32'**: Adding 32 to the ASCII value of 'D' (68) results in 100, which is the ASCII value of 'd'. Thus, the third character printed is 'd'.  
Therefore, the complete output is `characters: a C d`.

# Question 4

In C, if we declare an integer variable 'x' and assign it the value 10, and then declare a pointer variable 'ptr' and assign it the address of 'x', what do 'x', '&x', and 'ptr' each represent?

**Answer:**  
x = 10 (value), &x = address of x, ptr = address of x

**Solution:**  
Here's a breakdown:
- 'x': This represents the value of the variable, which is 10 in this case.
- '&x': This is the address-of operator. It gives you the memory location where the value of 'x' (which is 10) is stored. Think of it like the street address of a house.
- 'ptr': This pointer variable now holds the address of 'x'. It's like writing down the street address of 'x's house and storing it in 'ptr'. 'ptr' doesn't contain the value 10 itself, but it tells you where to find it.

# Question 5

In the C code snippet below, what are the values of *ptr and &var after the assignment?

```c
int var = 10;
int *ptr;
ptr = &var;
```

A) Both *ptr and &var are the memory address of var.  
B) Both *ptr and &var are 10.  
C) *ptr is 10, and &var is the memory address of var.  
D) *ptr is the memory address of var, and &var is 10.

**Answer: C**

**Solution:**  
1. `int var = 10;` declares an integer variable `var` and initializes it to 10.
2. `int *ptr;` declares a pointer variable `ptr` that can store the address of an integer.
3. `ptr = &var;` assigns the address of `var` to `ptr`. The & operator retrieves the memory address of var.
4. `*ptr` now refers to the value stored at the address pointed to by `ptr`, which is the value of `var` (10).
5. `&var` represents the memory address of the variable `var`.

# Question 6

Given the declaration `int arr[5] = {10, 20, 30, 40, 50};`, explain the equivalence between `arr` and `&arr[0]` and the difference between `arr + 1` and `&arr + 1`.  
What values do `*(arr + 2)` and `*(&arr[3])` represent?

**Answer:**  
`arr` and `&arr[0]` are equivalent, both representing the address of the first element.  
`arr + 1` points to the second element, while `&arr + 1` points to the location after the entire array.  
`*(arr + 2)` is 30, and `*(&arr[3])` is 40.

**Solution:**  
In C, the array name arr decays to a pointer to the first element of the array, which is equivalent to `&arr[0].` Thus, both represent the memory address of the first element (index 0) of the array.  
`arr + 1` represents the memory address of the second element (index 1). Pointer arithmetic considers the data type of the array elements. Since arr is an integer array, `arr + 1` increments the address by `sizeof(int)`.  
`&arr + 1`, however, increments the address by the size of the entire array, which is `sizeof(int) * 5`. This is because `&arr` is a pointer to the entire array, not just its first element.  
`*(arr + 2)` dereferences the address at `arr + 2`, effectively accessing the element at index 2, which is 30.  
`*(&arr[3])` dereferences the address of the element at index 3, which is the same as directly accessing `arr[3]`, resulting in the value 40.  

# Question 7

Given the C code snippet below, analyze the following statements about pointer arithmetic.  
Assume arr is an integer array of size 10 and ptr is an integer pointer.  
Indicate True or False for each statement.

```c
int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int *ptr = &arr[0];
```

- a) The expression `ptr + 3` points to the same memory location as `&arr[3]`.

**Answer: True**

**Solution:**  
Adding an integer `n` to a pointer moves the pointer forward by `n` elements of the pointer's type.  
In this case, `ptr + 3` moves the pointer forward by 3 integers, making it equivalent to `&arr[3]`.

- b) If `ptr` points to `arr[5]`, then `ptr - 2` points to `arr[3]`.

**Answer: True**

**Solution:**  
Subtracting an integer n from a pointer moves the pointer backward by `n` elements.  
If `ptr` points to `arr[5]`, then `ptr - 2` points to `arr[5-2]`, which is `arr[3]`.

- c) The expression `&arr[7] - &arr[2]` results in the value 5.

**Answer: True**

**Solution:**  
Subtracting two pointers that point to elements within the same array yields the integer difference between their indices.  
`&arr[7] - &arr[2]` is equivalent to `7 - 2`, which equals 5.

- d) If `ptr` points to `arr[0]`, the expression `*ptr + 1` is equivalent to `arr[1]`.

**Answer: False**

**Solution:**  
`*ptr` dereferences the pointer, accessing the value at the memory location it points to (which is `arr[0]`).  
Adding 1 to this value does not change the pointer's location; it simply adds 1 to the value of `arr[0]`.  
It does not access `arr[1]`.

# Question 8

In C, what are the potential dangers of using the indirection operator (*) on a pointer variable that has not been initialized?  
Explain why this is considered unsafe and what consequences might occur.

**Answer:**  
Dereferencing an uninitialized pointer leads to unpredictable behavior and program crashes due to attempts to access invalid memory locations.

**Solution:**  
An uninitialized pointer contains a garbage address.  
Dereferencing such a pointer (using the * operator) means attempting to access a memory location at this random address.  
This is dangerous for two main reasons:
1. Logical Error: The program's logic is flawed because it's trying to use a value from a memory location it shouldn't be accessing. The value at that address is unpredictable and unrelated to the intended data, leading to incorrect results or unexpected behavior.
2. Segmentation Fault/Program Crash: Operating systems have memory protection mechanisms. When a program tries to access memory it doesn't have permission to (like a random address pointed to by an uninitialized pointer), the OS terminates the program to prevent damage or security breaches. This often manifests as a "segmentation fault" or similar error.

# Question 9

Which of the following declarations defines a pointer to an array of 10 integer pointers?

A) int *p[10];  
B) int (*p)[10];  
C) int *(*p)[10];  
D) int **p[10];

**Answer: C**

**Solution:**
1. Start with the identifier 'p'.
2. Moving outwards, the closest element is * indicating 'p' is a pointer.
3. Next is [10], indicating 'p' is a pointer to an array of size 10.
4. Finally, * indicates the elements of the array are integer pointers.  
Therefore, the correct declaration is int *(*p)[10];
