#155 Min Stack

################################################################################################################################################################################
# BELOW CODE WITH TC = O(1) and SC = O(2N)


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    

# Your MinStack object will be instantiated and called as such:
commands = ["MinStack","push","push","push","getMin","pop","top","getMin"]
values = [[],[-2],[0],[-3],[],[],[],[]]


# Initialize the MinStack object
minStack = None

# Process the commands
results = []

for command, value in zip(commands, values):
    if command == "MinStack":
        minStack = MinStack()
        results.append(None)  # Initialization does not return a value
    elif command == "push":
        minStack.push(value[0])
        results.append(None)  # Push does not return a value
    elif command == "pop":
        minStack.pop()
        results.append(None)  # Pop does not return a value
    elif command == "top":
        results.append(minStack.top())
    elif command == "getMin":
        results.append(minStack.getMin())

# Print the results
print(results)

#################################################################################################################################################################################
# BELOW CODE WITH TC = O(1) and SC = O(N)

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val <= self.min:
            # Push the old minimum value
            self.stack.append(self.min)
            # Update the minimum value
            self.min = val
        # Push the actual value
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            # If the popped value is the current minimum, pop again to get the old minimum value
            self.min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

"""

# Example usage:
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())  # Returns -3
# minStack.pop()
# print(minStack.top())     # Returns 0
# print(minStack.getMin())  # Returns -2
