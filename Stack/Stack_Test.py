from Stack_Function import Stack

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.print()            # Output: Stack: [30, 20, 10]
    print(s.peek())      # Output: 30
    print(s.pop())       # Output: 30
    s.print()            # Output: Stack: [20, 10]
    print(s.is_empty())  # Output: False