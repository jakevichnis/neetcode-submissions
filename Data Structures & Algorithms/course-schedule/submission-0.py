class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

            # visitSet = all courses along the current DFS path
        visitSet = set()
        def dfs(crs):
            # base case
            if crs in visitSet:
                return False # we visited a course twice
            if preMap[crs] == []:
                # has no prereqs
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                # if we found one that can't be completed
                if not dfs(pre): return False
            visitSet.remove(crs)
            # clears the potentially redundant path
            preMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True # all courses can be completed

