class MinStack:
    def __init__(self):
        # The main stack stores all elements pushed.
        self.stack = []
        # The min_stack stores the minimum element encountered at each corresponding level
        # of the main stack. This allows O(1) retrieval of the current minimum.
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or the new value is less than or equal to the current minimum,
        # push it onto min_stack. Using '<=' ensures that duplicate minimums are handled
        # correctly, preventing issues if the actual minimum is popped later.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack")
        
        popped_val = self.stack.pop()
        # If the popped value was the current minimum (i.e., it's at the top of min_stack),
        # remove it from min_stack as well to maintain consistency.
        if popped_val == self.min_stack[-1]:
            self.min_stack.pop()
        return popped_val

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            raise IndexError("getMin from empty stack")
        # The minimum element is always at the top of the min_stack. This operation is O(1).
        return self.min_stack[-1]

# --- Demonstration ---
if __name__ == "__main__":
    print("Demonstrating Min Stack functionality:")
    min_stack = MinStack()

    print("\nPushing 3, 5, 2, 1, 4")
    min_stack.push(3)
    print(f"Pushed 3. Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 3

    min_stack.push(5)
    print(f"Pushed 5. Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 3

    min_stack.push(2)
    print(f"Pushed 2. Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 2

    min_stack.push(1)
    print(f"Pushed 1. Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 1

    min_stack.push(4)
    print(f"Pushed 4. Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 1

    print(f"\nTop element: {min_stack.top()}") # Expected Top: 4
    print(f"Current minimum: {min_stack.getMin()}") # Expected Min: 1

    print("\nPopping elements:")
    print(f"Popped: {min_stack.pop()}") # Popped 4
    print(f"Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 1

    print(f"Popped: {min_stack.pop()}") # Popped 1
    print(f"Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 2 (1 was the min, now 2 is)

    print(f"Popped: {min_stack.pop()}") # Popped 2
    print(f"Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 3

    print(f"\nTop element: {min_stack.top()}") # Expected Top: 5
    print(f"Current minimum: {min_stack.getMin()}") # Expected Min: 3

    print("\nPushing 0, -1")
    min_stack.push(0)
    print(f"Pushed 0. Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: 0

    min_stack.push(-1)
    print(f"Pushed -1. Stack: {min_stack.stack}, Current Min: {min_stack.getMin()}") # Expected Min: -1

    print(f"\nFinal minimum: {min_stack.getMin()}") # Expected Min: -1
