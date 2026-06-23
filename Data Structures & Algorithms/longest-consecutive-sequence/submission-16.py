class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set()
        setnums = set(nums)
        if len(nums) > 0:
            if len(nums) == 1 or (len(setnums) == 1 and 0 in setnums):
                return 1
            for item in setnums:
                if item - 1 in setnums:
                    continue
                cnt = 0
                while(item + 1 in setnums):
                    cnt += 1
                    item += 1
                cnt += 1
                count.add(cnt)
        else:
            return 0
        return max(count)
        
            