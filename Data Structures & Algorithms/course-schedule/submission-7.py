class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list mapping courses to prereqs
        # iterate through each course:
        # in each course, dfs each prereq to check if can be finished/cycle detection
        # visit set for cycle detection
        # after finishing a course: clear the prereqs so not repeat work

        graph = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course):
            if graph[course] == []:
                return True
            if course in visit:
                return False
            visit.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            graph[course] = []
            visit.remove(course)
            return True

        visit = set()
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
