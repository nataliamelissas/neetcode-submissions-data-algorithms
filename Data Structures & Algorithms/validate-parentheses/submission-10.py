class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # will only contain the opening characters
        closedToOpen = {')':'(', '}':'{', ']':'['} # maps opening to its closing character

        for c in s:
            if c in closedToOpen:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        