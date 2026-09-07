from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course]+=1

        q = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []

        while q:
            node = q.popleft()
            order.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return order if len(order) == numCourses else []



       
        

        