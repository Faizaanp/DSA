""" 
problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Examples

Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.

"""

import random
def secondLargest(array):
    largest = float("-inf")
    secondSmallest = float("-inf")
    
    for num in array:
        if num > largest:
            secondLargest = largest
            largest = num
        if num > secondLargest and num < largest:
            secondLargest = num
    
    return secondLargest
            

def secondSmallest(array):
    smallest = float("inf")
    secondSmallest = float("inf")
    
    for num in array:
        if num < smallest:
            secondSmallest = smallest
            smallest = num
        if num < secondSmallest and num > smallest:
            secondSmallest = num
            
    return secondSmallest

if __name__ == "__main__":
    array = [1,2,3,4,5] #[random.randint(0, 100) for _ in range(10)]
    print("Input:", array)
    print("Output:")
    print("\tSecond Smallest:", secondSmallest(array))
    print("\tSecond Largest:", secondLargest(array))
    
    