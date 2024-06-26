print("Enter your array: ")
str = input()
array = [int(value) for value in str.split(" ")]

print("Enter sum: ")
s = int(input())


def pair_of_given_sum_in_array(arr, sum):
    # Time Complexity: O(n^2)
    # Auxiliary Space Complexity: O(1)
    # Pros: Simple and straightforward implementation.
    # Cons: Inefficient for large arrays due to quadratic time complexity.
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                print(f"pair of sum: {arr[i]} + {arr[j]} = {sum}")


pair_of_given_sum_in_array(array, s)


def pair_using_dict(arr, target_sum):
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(n)
    # Pros: Significantly more efficient than the brute-force approach for large arrays.
    # Cons: Requires additional space proportional to the size of the array.
    seen = {}
    for num in arr:
        value = target_sum - num
        if value in seen:
            print(f"pair of sum: {value} + {num} = {target_sum}")

        seen[num] = True


pair_using_dict(array, s)


def pair_of_given_sum_in_sorted_array(arr, target_sum):
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    # Pros: Optimized for sorted arrays, leveraging the sorted nature to efficiently find pairs that sum to the target.
    # Cons: Requires the array to be sorted
    left = 0
    right = len(arr) - 1
    arr.sort()
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            print(f"pair of sum: {arr[left]} + {arr[right]} = {target_sum}")
            right -= 1
            left += 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1


pair_of_given_sum_in_sorted_array(array, s)
