class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        if n == 0:
            return []

        s = [temperatures[-1]]
        res = [0]

        for i in range(n-2, -1 ,-1):
            temp_s = s[:]
            counter = 1
            while len(s) > 0:
                if temperatures[i] >= s[-1]:
                    counter += 1
                    s.pop()
                else:
                    break
            if len(s) > 0:
                res.insert(0,counter)
            else:
                res.insert(0,0)
            s = temp_s
            s.append(temperatures[i])
            
        
        
        return res


        