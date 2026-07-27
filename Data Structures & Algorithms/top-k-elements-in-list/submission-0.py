class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a counter dictionaery to get the k ferquencies 
        #and use the max to get the highest
        seen = set()
        res = []
        freq = Counter(nums)
        while k > 0:
            most = max(freq,key = freq.get)
            if most not in seen:
             res.append(most)
             seen.add(most)
            else:
                del freq[most]
                most = max(freq,key = freq.get)
                res.append(most)
                seen.add(most)
            k -=1
        return res

        