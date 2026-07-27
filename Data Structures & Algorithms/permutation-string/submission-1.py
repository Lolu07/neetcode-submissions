class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l =0
        n = len(s1)
        s1_count = Counter(s1)

        while l + n <= len(s2):
            if Counter(s2[l:l+n]) == s1_count:
                return True
            l +=1
        return False

        