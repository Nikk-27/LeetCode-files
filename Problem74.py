# 74 Search a 2D Matrix

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Since the two binary searches are nested, the total time complexity is the product of the two: TC : O(log m)×O(log n)=O(log m ⋅ log n)
        row_l, row_r = 0, len(matrix) - 1  # Initialize row pointers for binary search
        l, r = 0, len(matrix[0]) - 1  # Initialize column pointers (though these are reset inside the loop)

        while row_l <= row_r:
            row_m = (row_l + row_r) // 2  # Find the middle row

            # If target is smaller than the first element of the middle row, search the upper half of the rows
            if matrix[row_m][0] > target:
                row_r = row_m - 1
            # If target is larger than the last element of the middle row, search the lower half of the rows
            elif matrix[row_m][-1] < target:
                row_l = row_m + 1
            else:
                # Perform binary search within the identified row
                l, r = 0, len(matrix[row_m]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[row_m][mid] > target:
                        r = mid - 1
                    elif matrix[row_m][mid] < target:
                        l = mid + 1
                    else:
                        return True  # Target found
                return False  # Target not found in the identified row

        return False  # Target not found in any row
            

        ''' mycode with for loop  TC : O(m \log n)
        for j in matrix:
        # O(m): Iterating through each row
            print(j)
            if target > j[-1]:
                print("BIG")
                continue
            elif target <= j[-1]:
            # O(log n): Binary search within the row
                print("SMALL")
                left, right = 0, len(j)-1
                while left <= right:
                    mid = left + ((right - left) // 2) # Overflow-Safe Middle Calculation
        
                    # Check if target is present at mid
                    if j[mid] == target:
                        return j, True
                    # If target is greater, ignore left half
                    elif j[mid] < target:
                        left = mid + 1
                    # If target is smaller, ignore right half
                    else:
                        right = mid - 1
        return False
        '''



matrix = [[1,5,5,6],[10,15,16,20],[23,31,34,60]]
target = 15
solution = Solution()
print(solution.searchMatrix(matrix, target))