from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		hash_table = {}
		for i in range(len(nums)):
			if target - nums[i] in hash_table:
				return [hash_table[target - nums[i]], i]
			hash_table[nums[i]] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))