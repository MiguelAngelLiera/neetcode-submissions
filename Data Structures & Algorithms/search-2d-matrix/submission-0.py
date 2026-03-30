class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        mid = int((n-1)/2)
        if n == 0:
            return False
        if n == 1:
            return self.binary_search(matrix[0], target)
        if matrix[mid][-1] > target:
            return self.searchMatrix(matrix[:mid+1], target)
        if matrix[mid][-1] < target:
            return self.searchMatrix(matrix[mid+1:], target)
        else:
            return True

    def binary_search(self, array: List[int], target: int) -> bool:
        m = len(array)
        mid = int(m/2)
        if m == 0:
            return False
        if m == 1:
            return array[0] == target
        if array[mid] > target:
            return self.binary_search(array[:mid], target)
        if array[mid] < target:
            return self.binary_search(array[mid:], target)
        else:
            return True
        