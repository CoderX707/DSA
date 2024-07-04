def sum_of_contiguous_arr(arr):
    # Computes the maximum sum of a contiguous subarray using Kadane's algorithm.

    # Time Complexity: O(n), where n is the length of the array.
    # Auxiliary Space Complexity: O(1) since it uses constant extra space.
    # Pros: Efficient and clear implementation leveraging Kadane's algorithm.
    # Cons: Assumes array contains at least one element. Relies on basic comparison operations.
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    print(f"Sum of contigous: {max_so_far}")


sum_of_contiguous_arr([1, 2, 3, -2, 5])


def sum_of_contiguous_arr1(arr):
    # Computes the maximum sum of a contiguous subarray using a linear scan approach.

    # Time Complexity: O(n), where n is the length of the array.
    # Auxiliary Space Complexity: O(1) since it uses constant extra space.
    # Pros: Simple and effective solution with linear time complexity.
    # Cons: Assumes array contains at least one element. Relies on basic comparison operations.
    max_ending = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < max_ending + arr[i]:
            max_ending = max_ending + arr[i]
        elif max_ending < arr[i]:
            max_ending = arr[i]
    print(f"Sum of contigous: {max_ending}")


sum_of_contiguous_arr1([1, 2, 13, -2, 5])
