""" 
Problem Statement: Given an array, we have to find the largest element in the array.

Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
"""
import random
#brute force approach
def findLargest(array):
    largestIndex = -1
    for i in range(len(array)):
        if largestIndex == -1 or array[largestIndex] < array[i]:
            largestIndex = i
    return array[largestIndex]

if __name__ == "__main__":
    list = [ random.randint(0, 100) for _ in range(10)]

    largestNum = findLargest(list)
    
    print("largest number in the array ", largestNum)

    assert largestNum == max(list), "The largest number is not found correctly"