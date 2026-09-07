class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        candidates.sort()


        def dfs(start, remaining):
            # each index chosen at most once in sol
            if remaining == 0:
                res.append(sol[:])
                return
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > remaining:
                    break

                sol.append(candidates[i])
                dfs(i+1, remaining - candidates[i])
                sol.pop()
            

        dfs(0, target)
        return res
