class Solution:
    def isPalindrome(self, s: str) -> bool:
        ##USE TWO POINTER -->

        #clean  the palindrome
        clean=[]
        for c in s:
            if c.isalnum():
                clean.append(c.lower())
        
        left=0
        right=len(clean)-1
        while left<right:
            if clean[left]!= clean[right]:
                return False
            left+=1
            right-=1
        return True
        
