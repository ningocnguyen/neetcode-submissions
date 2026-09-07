class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        def dfs(course, visit):
            if course in visit:
                return False
            
            if preMap[course] == []:
                return True
            
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