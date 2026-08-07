class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #solve it using hash
        s={}

        for index,num in enumerate(nums):
            complement=target-num

            if complement in s:
                return [s[complement],index]
            else:
                s[num]=index
        return[]