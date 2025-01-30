class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort (Kahn's Algorithm)
        incomingindices = [0] * numCourses
        adj = [[] for i in range(numCourses)] 
        for i,j in prerequisites:
            incomingindices[j] += 1
            adj[i].append(j)

        q = deque()
        for i in range(numCourses):
            if incomingindices[i] == 0:
                q.append(i)
        
        finish = 0

        while q:
            node = q.popleft()
            finish += 1
            for i in adj[node]:
                incomingindices[i] -= 1
                if incomingindices[i] == 0:
                    q.append(i)
        return finish == numCourses


# TC = O(V + E)
# SC = O(V + E)