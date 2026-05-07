class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #first len of arr count
        n=len(nums)

        #then we normalizeeee to stop unecessary rotation
        k=k%n

        #now lets make reverse function
        def reverse(start:int,end:int)->None:
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]  #swapping

                start+=1  #move both pointers
                end-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)