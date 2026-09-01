class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = "".join([char.lower() for char in s if char.isalnum()])

        backward = "".join([s[index].lower() for index in range(len(s)-1, -1, -1) if s[index].isalnum()])

        if forward == backward:
            return True
        
        return False