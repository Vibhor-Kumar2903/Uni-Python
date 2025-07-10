"""
Recursion:
Recursion is often more intuitive and easier to implement when the problem is naturally recursive, like tree traversals.
It can lead to solutions that are easier to understand compared to iterative ones.

Iteration:
Iteration involves loops (for, while) to repeat the execution of a block of code.
It is generally more memory-efficient as it does not involve multiple stack frames like recursion.
Advantages of using recursion

Simplicity: Recursive code is generally simpler and cleaner, especially for problems inherently recursive in nature (e.g., tree traversals, dynamic programming problems).
Reduced Code Length: Recursion can reduce the length of the code since the repetitive tasks are handled through repeated function calls.
Disadvantages of using recursion
Memory Overhead: Each recursive call adds a new layer to the stack, which can result in significant memory use, especially for deep recursion.

Performance Issues: Recursive functions may lead to slower responses due to overheads like function calls and returns.
Risk of Stack Overflow: Excessive recursion can lead to a stack overflow error if the recursion depth exceeds the stack limit.

Recursion in Python – FAQs
What is Recursion in Python?
Recursion in Python refers to a function calling itself during its execution. This programming technique is used to solve problems that can be broken down into simpler, repetitive tasks. Each recursive call reduces the problem into a smaller piece, and recursion continues until it reaches a base case, which does not involve a recursive call. Recursive functions are commonly used in tasks like traversing data structures (e.g., trees or graphs) and solving algorithmic problems (e.g., sorting or computing factorials).
"""

def factorial(n):
    if n==0:
        fact = 1
    else:
        fact =  n * factorial(n-1)
    return fact

print(factorial(5))

