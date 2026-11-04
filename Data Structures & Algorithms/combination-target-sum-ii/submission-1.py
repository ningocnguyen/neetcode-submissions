class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur, res = [], []


        def backtrack(level, remaining):
            if remaining == 0:
                res.append(cur[:])
                return
            for i in range(level, len(candidates)):
                # we've already explored this value at this recursion level
                # i>start very important!!
                if i>level and candidates[i] == candidates[i-1]:
                    continue
                if remaining < candidates[i]:
                    return
                # include
                cur.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])

                # exclude
                cur.pop()



        backtrack(0, target)
        return res
