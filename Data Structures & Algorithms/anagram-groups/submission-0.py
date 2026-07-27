class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group anagrams into a sublist
        #i.e strings that contain exact smae characters
        arr = []
        res = []
        groups = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            arr.append(sorted_str)
            groups[sorted_str].append(s)
            
        for i in groups:
            res.append(groups[i])
        return res


        