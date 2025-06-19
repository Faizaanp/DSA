""" 
insertion sort
inserts each element into correct position 
"""

import random

def insertionSort(array):
    arrayLen = len(array)
    for i in range(1, arrayLen):
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array

if __name__ == "__main__":
    list = [random.randint(0, 100) for x in range(10)]
    print("Unsorted list:", list)
    sortedList = insertionSort(list)
    print("Sorted list:", sortedList)

    assert sortedList == sorted(list), "The list is not sorted correctly"