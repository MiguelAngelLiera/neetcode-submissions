class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        N = len(arr)
        i = N - 1
        for idx,n in enumerate(arr):
            if n >= x:
                i = idx
                break 
        j = i - 1
        while k > 0:
            a = arr[j] if j > -1 else float('inf')
            b = arr[i] if i < N else float('inf')
            d1 = abs(a - x)# if j > -1 else float('inf')
            d2 = abs(b - x)# if i < N else float('inf')
            if (d1 < d2 or d1 == d2 and a < b) and a != float('inf'):
                res = arr[j:j+1] + res
                j -= 1
            elif b != float('inf'):
                res += arr[i:i+1]
                i += 1
            k -= 1
        return res

            
        
                

    
        