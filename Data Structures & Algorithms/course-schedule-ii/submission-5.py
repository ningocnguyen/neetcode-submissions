class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list mapping course to prereqs
        # visit set to track current in dfs path
        # completed set to track fully processed course so not visited again
        # append all fully processed course to order list


        graph = {course:[] for course in range(numCourses)}
        order = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        

        def dfs(course):
            if course in visit:
                return False
            if course in completed:
                return True
            visit.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            completed.add(course)
            # graph[course] = []
            order.append(course)
            return True

        visit = set()
        completed = set()
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order
        


        
