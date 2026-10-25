class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build an adjacency list mapping each course to its prereq
        # initiate a visit set to track currently explored course
        # run dfs for each course
        # if a course already in visit --> theres a cycle --> return False
        # after finishing a course, clear the prereq so we dont repeat work

        graph = {course: [] for course in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def dfs(course, visit):
            if course in visit:
                return False
            if graph[course] == []:
                return True
            visit.add(course)
            for pre in graph[course]:
                if not dfs(pre, visit):
                    return False
            visit.remove(course)
            graph[course] = []
            return True
        
        visit = set()
        for course in range(numCourses):
            if not dfs(course, visit):
                return False
        return True
