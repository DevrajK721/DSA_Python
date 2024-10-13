class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []

    def push(self, value):
        # Push a value onto the stack
        self.stack.append(value)

    def pop(self):
        # Pop and return the top value from the stack (if it's not empty)
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty!")
            return None

    def peek(self):
        # Return the top value without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def size(self):
        # Return the size of the stack
        return len(self.stack)

    def print(self):
        # Print the stack (from top to bottom)
        print("Stack:", self.stack[::-1])