class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking
        cur, res = [], []
        n=len(nums)
        nums.sort()

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(cur[:])
                return

            if i>=n or remaining<nums[i]:
                return
            
            # include
            cur.append(nums[i])
            backtrack(i, remaining-nums[i])

            # exclude
            cur.pop()
            backtrack(i+1, remaining)

        backtrack(0, target)
        return res