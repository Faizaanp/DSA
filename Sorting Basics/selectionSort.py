""" 
selection sort 
selects the smallest and put in the first position
repeats the process for the rest of the list
Time complexity: O(n^2)
"""
import random
def selectionSort(array):
    arrayLen = len(array)
    for i in range(arrayLen):
        minIndex = i
        # find the minimum element
        for j in range(i + 1, arrayLen):
            if array[minIndex] > array[j]:
                minIndex = j
                
        # swap the found minimum element with ith element
        array[i], array[minIndex] = array[minIndex], array[i]

    return array

if __name__ == "__main__":
    list = [random.randint(0, 100) for x in range(10)]
    print("Unsorted list:", list)
    sortedList = selectionSort(list)
    print("Sorted list:", sortedList)
    
    
    assert sortedList == sorted(list), "The list is not sorted correctly"