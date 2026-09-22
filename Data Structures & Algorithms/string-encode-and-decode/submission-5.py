class Solution:

    def encode(self, strs: List[str]) -> str:
       result = ""
       for s in strs:
        length = len(s)
        result += str(length) + '#' + s
        
       return result
            


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0


        while i < len(s):
            temp = ""
            while s[i].isdigit():
                temp +=s[i]
                i +=1


            length = int(temp)
            count = 0
            i +=1
            decoded_str = []
            while i < len(s) and count < length:
                decoded_str.append(s[i])
                count +=1
                i +=1
            result.append("".join(decoded_str))

        return result



        

