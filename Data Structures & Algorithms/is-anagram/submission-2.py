class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if s andd t are anagrams of each other
        #anagram is a string that has the exact same characters as another string
        #but order of characters can differ
        #create a counter for the two strings to check each character occurence

        s_count = Counter(s)
        t_count = Counter(t)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s_count[s[i]] != t_count[s[i]]:
                return False
        return True
        