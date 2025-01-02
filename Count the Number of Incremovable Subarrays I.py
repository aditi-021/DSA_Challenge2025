class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        N = len(nums)

        #program to check if the remaining array(after subtracting subarray from main array ) is increasing or not 
        def good(arr):
            for x, y in zip(arr, arr[1:]):
                if x>= y:
                    return False
            return True

        count = 0
        for i in range(N):
            for j in range(i, N):
                x = []
                for k in range(N):
                    if not (i<= k<= j):
                        x.append(nums[k])
                if good(x):
                    count += 1
        return count 
