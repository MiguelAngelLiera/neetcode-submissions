class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        aps = {}
        for i, c in enumerate(s):
            if c not in aps.keys():
                aps[c] = [i, i+1]
            else:
                if i + 1 == 10:
                    print(c)
                aps[c][1] = i + 1
                j = aps[c][0]
                for k, v in aps.items():
                    if v[0] <= j < v[1]:
                        aps[k] = [v[0], i + 1]
                        aps[c][0] = v[0]
                    if j <= v[0]:
                        aps[k] = [j, i+ 1]

        print(aps)
        
        arrays = list(set([tuple(v) for v in aps.values()]))
        arrays.sort()
        distances = []
        for a in arrays:
            #if a[1] - a[0] not in distances:
            distances.append(a[1] - a[0])

        return distances

        