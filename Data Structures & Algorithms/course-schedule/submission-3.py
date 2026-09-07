class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)} # set up so that courses without prereq dont get dropped
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        def dfs(course, visit):
            if preMap[course] == []:
                return True
            if course in visit:
                return False
            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre, visit):
                    return False

            visit.remove(course)
            preMap[course] = []
            return True

        visit = set()
        for course in range(numCourses):
            if not dfs(course, visit):
                return False

        return True