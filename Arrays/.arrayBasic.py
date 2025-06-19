""" 
array basic operations
- create an array
- access an element
- update an element
- delete an element
- iterate through an array
- find the length of an array
- check if an element exists in an array
- reverse an array
- sort an array
- concatenate two arrays
- slice an array
- copy an array


"""

def arrayOperations(array):
    # Create an array
    print("Original array:", array)

    # Access an element
    print("Element at index 2:", array[2])

    # Update an element
    array[2] = 10
    print("Updated array:", array)

    # Delete an element
    del array[2]
    print("Array after deletion:", array)

    # Iterate through an array
    print("Iterating through the array:")
    for element in array:
        print(element, end=' ')
    print()

    # Find the length of an array
    print("Length of the array:", len(array))

    # Check if an element exists in an array
    print("Does 5 exist in the array?", 5 in array)

    # Reverse an array
    reversed_array = list(reversed(array))
    print("Reversed array:", reversed_array)

    # Sort an array
    sorted_array = sorted(array)
    print("Sorted array:", sorted_array)

    # Concatenate two arrays
    another_array = [20, 30, 40]
    concatenated_array = array + another_array
    print("Concatenated array:", concatenated_array)

    # Slice an array
    sliced_array = concatenated_array[1:4]
    print("Sliced array (index 1 to 3):", sliced_array)

    # Copy an array
    copied_array = concatenated_array.copy()
    print("Copied array:", copied_array)
    
if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5]
    arrayOperations(sample_array)
    
    
    
    
    

