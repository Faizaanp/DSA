""" 

(leetcode 485)
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxOnes = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                maxOnes = max(maxOnes, ones)
                ones = 0
        return max(maxOnes, ones)

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print("Maximum consecutive 1's in", nums, "is:", sol.findMaxConsecutiveOnes(nums))

    nums = [1, 0, 1, 1, 0, 1]
    print("Maximum consecutive 1's in", nums, "is:", sol.findMaxConsecutiveOnes(nums))
    nums = [0, 0, 0]
    print("Maximum consecutive 1's in", nums, "is:", sol.findMaxConsecutiveOnes(nums))