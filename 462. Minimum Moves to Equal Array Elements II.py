class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n%2 == 0 :
            med = (nums[(n//2)-1] + nums[(n//2+1)-1])//2
        else:
            med = nums[((n+1)//2)-1]

        count = 0
        for num in nums:
            count = count + (abs(num-med))
        
        return count
