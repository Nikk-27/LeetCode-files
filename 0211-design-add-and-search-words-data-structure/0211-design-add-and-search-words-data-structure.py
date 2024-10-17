class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            cur = node

            for i in range(index, len(word)):
                c = word[i]
                
                # If it's a wildcard '.'
                if c == '.':
                    # Check all possible children nodes
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                # If the character doesn't exist in current node's children
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.endOfWord
        
        return dfs(0, self.root)


'''
Time Complexity
addWord(word: str):

Inserting a word involves adding each character, which takes O(n) time, where n is the length of the word.
search(word: str):

In the worst case, searching with wildcards can explore multiple branches, leading to a time complexity of O(26^n) in the worst-case scenario (when every character is a wildcard, and there are 26 possible children for each node). However, typically the search will be more efficient when fewer wildcards are used.
Space Complexity
The space complexity for addWord is O(n) per word, where n is the number of characters in the word, due to the Trie structure's creation of new nodes for each character.

Example with "...." (4 wildcards):
If you are searching for "...." (4 wildcards) in a Trie, the search will explore:

At level 1: 26 possibilities.
At level 2: 26 possibilities for each of the 26 branches from level 1.
At level 3: 26 possibilities for each of the 26 branches from level 2.
At level 4: 26 possibilities for each of the 26 branches from level 3.
This results in 
26×26×26×26=26^4=456,976 potential branches to explore in the worst-case scenario.

Summary
Worst-Case Scenario: When searching for a word made up entirely of wildcards (.), the search needs to explore all possible branches of the Trie.
Exponential Growth: The number of branches grows exponentially with the length of the word, leading to a worst-case time complexity of O(26^n), where n is the number of wildcards.
'''