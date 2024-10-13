# DSA_Python
A range of data structures and algorithms implemented in Python

## Arrays & Hashing
### Arrays
Arrays are data structures that store collections of elements in a contiguous block of memory. Arrays allow you to store multiple values in a single variable which can be accessed using indices.

In Python, arrays are most commonly referred to as lists. They are dynamic and can be used to store elements of different types but are usually used to store elements of the same type.

### Hashing
Hashing is a process used in many data structures like hash tables, hashsets and dictionaries where a key is mapped to a value using a hash function. The hash function takes an input (key) and returns an integer known as a hash value. 

In Python, hashing is heavily utilized in dictionaries and sets. 

[Arrays and Hashing](Arrays_and_Hashing)

## Stack
### Key Operations:

1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove and return the top element of the stack.
3. **Peek (or Top)**: Return the top element without removing it.
4. **isEmpty**: Check if the stack is empty.
5. **isFull** (for fixed-size stacks): Check if the stack is full (rare in dynamic implementations).

### How It Works:

- A stack can be implemented using arrays or linked lists. In an array, the last element represents the "top" of the stack, while in a linked list, the head node often serves this role.
- Every time an element is pushed onto the stack, it becomes the new top. When an element is popped, the current top is removed, and the next element below becomes the new top.

### Common Use Cases:

1. **Reversing**: Reversing strings or lists can be done easily by pushing each element onto a stack and then popping them off in reverse order.
2. **Parentheses Matching**: Stacks are used to validate expressions with parentheses, brackets, or braces by ensuring they open and close in the correct order.
3. **Backtracking**: When exploring paths (e.g., in maze problems), stacks help track the sequence of choices, allowing for backtracking to previous states.
4. **Function Call Management**: Recursion is managed via a system stack, where function calls are pushed when invoked and popped when completed.
5. **Depth-First Search (DFS)**: Stack is used to implement DFS in both trees and graphs.

### Time Complexity:

- **Push**: $O(1) $– Adding an element is a constant-time operation.
- **Pop**: $O(1)$ – Removing the top element is also constant-time.
- **Peek**: $O(1)$ – Viewing the top element doesn't involve traversal.

### Space Complexity:

- The space complexity depends on the number of elements in the stack, typically $O(n)$, where `n` is the number of elements in the stack.

### When to Use:

- When you need to process elements in a **reverse order** of insertion.
- When solving problems involving **nested structures** (like parentheses or function calls).
- When using algorithms that involve **backtracking** (e.g., DFS, pathfinding).

### Stack Variations:

1. **Monotonic Stack**: A special type of stack where elements are ordered either increasingly or decreasingly. Commonly used in problems that require finding the next or previous greater/smaller element.
2. **Fixed vs Dynamic Stack**: A stack with a fixed size (array implementation) vs. one that grows dynamically (linked list implementation).


[Stack](Stack)