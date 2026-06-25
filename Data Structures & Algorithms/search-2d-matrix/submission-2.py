class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def convertTo2D(matrix: List[List[int]], index: int) -> List[int]:
        #     pass

        m = len(matrix)
        n = len(matrix[0]) 
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (right + left) // 2

            mid_row, mid_col = mid // n, mid % n

            if matrix[mid_row][mid_col] < target:
                left = mid + 1
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
            else:
                return True
        
        return False