#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(0,len(nums)-1):
            for index2 in range(index1+1,len(nums)):
                if target == nums[index1] + nums[index2]:
                    return (index1, index2)
