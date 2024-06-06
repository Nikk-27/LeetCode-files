#155 Min Stack

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
