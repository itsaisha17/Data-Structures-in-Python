class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        left=0              #start 
        right=0
        max_len=0

        for right in range(len(s)):
            while s[right] in char_set:
                #if found then remove and move left pointer fwd
                char_set.remove(s[left])
                left+=1

            #else if not found then add
            char_set.add(s[right])

            #take max of length of all and then return
            max_len=max(max_len,right-left+1)
        return max_len
        
        