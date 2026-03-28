#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.cn/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (75.61%)
# Likes:    847
# Dislikes: 0
# Total Accepted:    151.7K
# Total Submissions: 200.6K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an integer array nums of length n where all the integers of nums are in
# the range [1, n] and each integer appears at most twice, return an array of
# all the integers that appears twice.
# 
# You must write an algorithm that runs in O(n) time and uses only constant
# auxiliary space, excluding the space needed to store the output
# 
# 
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
# Input: nums = [1]
# Output: []
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res = []
        # n = len(nums)
        # # 4, 2, 3, 1
        # # cyclic sort
        # for i in range(n): # i = 0;
        #     while nums[i] != nums[nums[i] - 1]: # we should not swap if two numbers are same
        #         # 4, 1 -> correct = 3 -> so the correct position is nums[3] so we should swap first and the nums[3]
        #         correct_idx = nums[i] - 1
        #         nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # # collect duplicates
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         res.append(nums[i])
        
        # return res
        res=[]
        #4,3,1,2,2
        for x in nums:
            idx = abs(x) - 1 # idx=3 -> num=2; idx=2 -> num=1; idx=0 -> num=4; idx=1 -> num=3; idx=1 -> num=-3
            if nums[idx] < 0:
                res.append(idx + 1) #append abs(x) - 1 + 1 -> which is the answer
            else:
                nums[idx] = -nums[idx] # 4,3,1,-2,2; 4,3,-1,-2,2; -4,3,-1,-2,2; -4,-3,-1,-2,2
        return res

        
# @lc code=end

