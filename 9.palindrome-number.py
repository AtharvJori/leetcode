#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            print(False)
        else:
           if str(x) == reversed(str(x)):
               print(True)
       

c = Solution()     
c.isPalindrome(-121)

        

        
# @lc code=end

