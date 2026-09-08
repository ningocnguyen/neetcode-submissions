class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # space: O(n)
        row = [1] * n

        for _ in range(m - 1):
            for c in range(1, n):
                row[c] = row[c] + row[c - 1]

        return row[-1]