class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}':'{', ']':'['}
        stack = []
        open_count = 0
        close_count = 0
        for char in s:
            if char not in char_map:
                stack.append(char)
                open_count +=1
            else:
                if stack and stack.pop() != char_map[char]:
                    return False
                close_count +=1
        if close_count != open_count:
            return False
        if stack:
            return False
        return True
        