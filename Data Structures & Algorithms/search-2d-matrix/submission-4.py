class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log) time and sorted -> binary search
        # search row by row with binary search

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if target == matrix[i][n-1]:
                return True
            elif target < matrix[i][n-1]:
                l, r = 0, n-1
                while l<=r:
                    mid = (l+r)//2
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        r=mid-1
                    else:
                        l=mid+1
            else:
                continue

        return False
