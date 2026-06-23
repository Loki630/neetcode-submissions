class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = left + 1
        length = len(numbers)
        while(left < right and left != length):
            if right != length and numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if right == length:
                left += 1
                right = left + 1
                continue
            right += 1
        return []