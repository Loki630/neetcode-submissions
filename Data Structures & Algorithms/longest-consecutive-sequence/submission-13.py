class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = []
        setnums = set(nums)
        iteration = []
        if len(nums) > 0:
            if len(nums) == 1 or (len(setnums) == 1 and 0 in setnums):
                return 1
            for item in setnums:
                if item in iteration:
                    continue
                lst = []
                while(item + 1 in setnums):
                    lst.append(item)
                    item += 1
                lst.append(item)
                iteration += lst
                count.append(len(lst))
        else:
            return 0
        return max(count)
        
            