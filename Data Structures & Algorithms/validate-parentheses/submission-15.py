class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_para = ['(', '{', '[']
        for char in s:
            if char in open_para:
                stack.append(char)

            elif not stack:
                return False
        
            if char == ')' and stack[-1] == '(':
                stack.pop()

            elif char == '}' and stack[-1] == '{':
                stack.pop()

            elif char == ']' and stack[-1] == '[':
                stack.pop()

            elif char in [')', '}', ']']:
                return False

        return not bool(stack)