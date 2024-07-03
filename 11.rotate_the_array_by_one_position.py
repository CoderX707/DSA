def rotate_array_by_one_position(arr):
    # Rotates the given array by one position in a clockwise direction using a custom implementation.

    # Time Complexity: O(n), where n is the length of the array.
    # Auxiliary Space Complexity: O(n) due to the use of an additional list (temp).
    # Pros: Demonstrates understanding of array indexing and custom logic.
    # Cons: Uses additional space proportional to the size of the array.
    n = len(arr) - 1
    temp = []
    for i in range(0, n):
        if i == 0:
            temp.append(arr[n])
            temp.append(arr[i])
        else:
            temp.append(arr[i])

    print(f"Rotated array: {temp}")


rotate_array_by_one_position([9, 8, 7, 6, 4, 2, 1, 3])


def rotate_array_inbuilt(arr):
    # Rotates the given array by one position in a clockwise direction using built-in functions.

    # Time Complexity: O(n), where n is the length of the array.
    # Auxiliary Space Complexity: O(1) since it modifies the array in place.
    # Pros: Simple and concise implementation using built-in functions.
    # Cons: Relies on the availability of built-in functions.
    if len(arr) == 0:
        return arr
    last_element = arr.pop()
    arr.insert(0, last_element)
    print(f"Rotated array: {arr}")


rotate_array_inbuilt([9, 8, 7, 6, 4, 2, 1, 3])


def rotate_array(arr):
    # Rotates the given array by one position in a clockwise direction using custom logic without built-in functions.

    # Time Complexity: O(n), where n is the length of the array.
    # Auxiliary Space Complexity: O(1) since it modifies the array in place.
    # Pros: Efficient in terms of space, does not use additional space proportional to the array size.
    # Cons: Slightly more complex to implement compared to using built-in functions.
    if len(arr) == 0:
        return arr
    n = len(arr)
    last_element = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element
    print(f"Rotated array: {arr}")


rotate_array([1, 2, 3, 4])
