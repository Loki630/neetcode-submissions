class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)

        indices = []
        for i in range(len(arr)):
            num = arr[i]
            left = 0
            right = len(arr) - 1
            while left < right:
                if right == i or left == i:
                    left += 1
                    continue
                if num + arr[left] + arr[right] < 0:
                    left += 1
                elif num + arr[left] + arr[right] > 0:
                    right -= 1
                else:
                    if (sorted([num,arr[left],arr[right]])) in indices:
                        left += 1
                        continue
                    indices.append(sorted([num,arr[left],arr[right]]))
                    left += 1
                    
        return indices