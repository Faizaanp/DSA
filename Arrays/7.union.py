""" Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.NOTE: Elements in the union should be in ascending order.

Examples

Example 1:
Input:
n = 5,m = 5.
arr1[] = {1,2,3,4,5}  
arr2[] = {2,3,4,4,5}
Output:
 {1,2,3,4,5}
 """
 
class Solution:
    def findUnion(self, arr1, arr2):
        unionSet = set()
        for num in arr1:
            if num in arr2:
                unionSet.add(num)
        for num in arr2:
            if num in arr1:
                unionSet.add(num)
        return sorted(unionSet)
    
if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 4, 4, 5]
    print("Union of arr1 and arr2:", sol.findUnion(arr1, arr2))
   