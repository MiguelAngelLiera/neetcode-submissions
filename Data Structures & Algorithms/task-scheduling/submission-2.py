import heapq as hq
class Solution:
    from collections import Counter
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        priority = []
        total = 0
        for k, v in counts.items():
            hq.heappush_max(priority, (v, k))

    
        while priority:
            out = []
            for i in range(n+1):
                if priority:
                    
                    count, fst = hq.heappop_max(priority)
                    if count > 1:
                        out.append((count - 1, fst))
                
                total += 1
                if not out and not priority:
                    break
                
            for o in out:
                hq.heappush(priority, o)
         
        return total





        