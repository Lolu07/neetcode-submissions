class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {']':'[', '}':'{', ')':'('}
        stack = []

        for char in s:
            if char not in close_open:
                stack.append(char)
            else: 
                if stack:             
                    if close_open[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return True if len(stack) == 0 else False




      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # char_map = {')': '(', '}':'{', ']':'['}
        # stack = []
        # open_count = 0
        # close_count = 0
        # for char in s:
        #     if char not in char_map:
        #         stack.append(char)
        #         open_count +=1
        #     else:
        #         if stack and stack.pop() != char_map[char]:
        #             return False
        #         close_count +=1
        # if close_count != open_count:
        #     return False
        # if stack:
        #     return False
        # return True
        