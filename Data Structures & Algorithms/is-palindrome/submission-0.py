class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            
            if s[i].isalnum():
                res.append(s[i].lower())
        
        n,m = 0, len(res)-1
        while n< m:
            if res[n] != res[m]:
                return False
            n +=1
            m -=1
        return True
        """
        return res[:len(res)+1] == res[len(res)-1::-1]
        """

            

        