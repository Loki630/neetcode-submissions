class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = []
        if len(nums) > 0:
            if len(nums) == 1 or (len(set(nums)) == 1 and 0 in set(nums)):
                return 1
            for item in set(nums):
                lst = []
                while(item + 1 in set(nums)):
                    lst.append(item)
                    item += 1
                lst.append(item)
                count.append(len(lst))
        else:
            return 0
        return max(count)
        
            