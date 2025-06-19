""" 
bubble Sort
just swap adjacents if they are in the wrong order
"""
import random
def bubbleSort(array):
    arrayLen = len(array)
    for i in range(arrayLen):
        for j in range(i + 1, arrayLen):
            # swap if the current element is greater than the next element
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

if __name__ == "__main__":
    list = [random.randint(0, 100) for x in range(10)]
    print("Unsorted list:", list)
    sortedList = bubbleSort(list)
    print("Sorted list:", sortedList)

    assert sortedList == sorted(list), "The list is not sorted correctly"
    