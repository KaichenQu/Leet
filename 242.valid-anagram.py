#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (67.31%)
# Likes:    1103
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s.length && t.length
        return Counter(s) == Counter(t)
# @lc code=end

