from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for h in range(len(nums)):
            for i in range(len(nums)):
                if h != i and (nums[h] + nums[i]) == target:
                    return [h, i]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4,], 6))
    print(s.twoSum([3,3,], 6))
