""" 
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

"""

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n 
        if k ==0:
            return nums
        nums[:] = nums[-k:] + nums[:-k]
        
        
            
            
        
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    print("Rotated array:", nums)
    
    assert nums == [5, 6, 7, 1, 2, 3, 4], "The array is not rotated correctly"
    
    nums = [-1, -100, 3, 99]
    k = 2
    solution.rotate(nums, k)
    print("Rotated array:", nums)
    
    assert nums == [3, 99, -1, -100], "The array is not rotated correctly"
    nums = [1, 2, 3, 4, 5]
    k = 0   
    solution.rotate(nums, k)
    print("Rotated array with k=0:", nums)  
    
    assert nums == [1, 2, 3, 4, 5], "The array should remain unchanged when k=0"