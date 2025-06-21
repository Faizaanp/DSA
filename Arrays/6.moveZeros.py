""" 
(LeetCode 283)
moveZeros 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 """
 
 
class Solution(object):
    def moveZeroes(self, nums):
        
        temp = list()
        for num in nums:
            if num != 0:
                temp.append(num)
        n = len(temp)
        nums[:n] = temp
        nums[n:] = [0] * (len(nums) - n)
        return nums 
if __name__ == "__main__":
    sol = Solution()
    
    nums = [0, 1, 0, 3, 12]
    print("Original array:", nums)
    sol.moveZeroes(nums)
    
    print("Array after moving zeros:", nums)
    
    assert nums == [1, 3, 12, 0, 0], "The array is not modified correctly"
    nums = [0]
    sol.moveZeroes(nums)
    print("Array after moving zeros:", nums)
    assert nums == [0], "The array is not modified correctly"
    nums = [1, 2, 3, 4]
    sol.moveZeroes(nums)
    print("Array after moving zeros:", nums)

    assert nums == [1, 2, 3, 4], "The array is not modified correctly"
    nums = [0, 0, 0, 0]
    sol.moveZeroes(nums)
    print("Array after moving zeros:", nums)

    assert nums == [0, 0, 0, 0], "The array is not modified correctly"