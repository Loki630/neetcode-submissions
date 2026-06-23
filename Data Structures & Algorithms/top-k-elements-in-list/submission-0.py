class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {num : nums.count(num) for num in set(nums)}
        sorted_dict = {u : v for u,v in (sorted(dict1.items(),key=lambda item : item[1],reverse = True))}
        final_list = [list(sorted_dict.keys())[i] for i in range(k)]
        return final_list