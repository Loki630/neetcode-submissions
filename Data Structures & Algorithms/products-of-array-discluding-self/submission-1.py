class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            num = nums[0::]
            num[i] = 1
            n = math.prod(num)
            output.append(n)
            del num
        return output