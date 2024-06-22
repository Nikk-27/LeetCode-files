# 981 Time Based Key-Value Store

from collections import defaultdict

class TimeMap:                                                                        # TC: O(LogN)

    def __init__(self):
        self.multi_value_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.multi_value_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        v = self.multi_value_dict.get(key, [])
        low = 0
        high = len(v) - 1
        return_value = ""

        while low <= high:
            mid = low + (high - low) // 2
            if v[mid][1] <= timestamp:
                return_value = v[mid][0]
                low = mid + 1
            elif v[mid][1] == timestamp:
                return_value = v[mid][0]
            else:
                high = mid - 1
            
        return return_value                                              
        
# Output : [null, null, "bar", "bar", null, "bar2", "bar2"]

# commands = ["TimeMap", "set", "get", "get", "set", "get", "get"]
# key_value_timestamp = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

commands = ["TimeMap","set","set","get","get","get","get","get"]
key_value_timestamp = [[],["love","high",40],["love","low",52],["love",5],["love",10],["love",15],["love",40],["love",25]]


# Process the commands
results = []

for command, value in zip(commands, key_value_timestamp):
    if command == "TimeMap":
        obj = TimeMap()
        results.append(None)  # Initialization does not return a value
    elif command == "set":
        obj.set(value[0], value[1], value[2])
        results.append(None)  # Set does not return a value
    elif command == "get":
        # obj.get(value[0], value[1])
        res_value = obj.get(value[0], value[1])
        results.append(res_value)  # Get does return a value

# Print the results
print(results)