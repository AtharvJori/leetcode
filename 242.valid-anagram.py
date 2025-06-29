#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0)+ 1
        for ch in t:
            if ch not in count:
                return False
                
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True
            



        
# @lc code=end

