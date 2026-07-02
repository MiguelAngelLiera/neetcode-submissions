class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        if N == 0:
            return arr
        greatest = arr[-1]
        arr[-1] = -1
        for i in range(N-2, -1, -1):
            a = arr[i]
            arr[i] = greatest 
            greatest = max(greatest  , a)
        return arr