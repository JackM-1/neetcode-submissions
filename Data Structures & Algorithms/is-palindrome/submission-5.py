class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1
        clean = s.lower()
        while l < r: 
            while l < r and not clean[r].isalnum():
                r -= 1 
            while l < r and not clean[l].isalnum():
                l += 1 
            if clean[l] != clean[r]:
                print(clean[l])
                return False
            l += 1 
            r -= 1
        return True