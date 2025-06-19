""" 
(leetcode)
1752. Check if Array Is Sorted and Rotated
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 
"""


class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
            if count > 1:
                return False
        return True
    

if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    solution = Solution()
    result = solution.check(nums)
    print("Is the array sorted and rotated?", result)
    
    assert result == True, "The array is not sorted and rotated correctly"
    
    nums = [2, 1, 3, 4]
    result = solution.check(nums)
    print("Is the array sorted and rotated?", result)
    
    assert result == False, "The array is incorrectly identified as sorted and rotated"
