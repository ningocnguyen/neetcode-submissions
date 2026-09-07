class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) 
        l = 0
        r = n-1
        
        for i in range(m):
            if target == matrix[i][n-1]:
                return True
            elif target < matrix[i][n-1]:
                while l<=r:
                    mid = l + (r-l) // 2
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                continue

        return False