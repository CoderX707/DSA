def count_union_elements(arr1, arr2):
    # Counts the number of unique elements in the union of two arrays.

    # Time Complexity: O(m + n), where m and n are the lengths of arr1 and arr2 respectively.
    # Auxiliary Space Complexity: O(m + n) due to the use of a set to store unique elements.
    # Pros: Simple and straightforward implementation.
    # Cons: Uses additional space proportional to the combined size of arr1 and arr2.
    combined_arr = arr1 + arr2
    union_set = set(combined_arr)
    print(f"Count is: {len(union_set)}")


count_union_elements([1, 32, 3, 24, 5], [1, 12, 3])


def find_union_count_for_sorted_arr(arr1, arr2):
    # Finds the number of unique elements in the union of two sorted arrays.

    # Time Complexity: O(m + n), where m and n are the lengths of arr1 and arr2 respectively.
    # Auxiliary Space Complexity: O(m + n) due to the use of a list to store unique elements.
    # Pros: Operates in linear time.
    # Cons: Requires the arrays to be sorted; additional space is used.
    union_arr = []
    for num in arr1:
        if num not in union_arr:
            union_arr.append(num)

    for num1 in arr2:
        if num1 not in union_arr:
            union_arr.append(num1)

    print(f"Count is: {len(union_arr)}")


find_union_count_for_sorted_arr([1, 32, 3, 24, 5], [1, 12, 3])


def union_using_dict(arr1, arr2):
    # Finds the number of unique elements in the union of two arrays using a dictionary.

    # Time Complexity: O(m + n), where m and n are the lengths of arr1 and arr2 respectively.
    # Auxiliary Space Complexity: O(m + n) due to the use of a dictionary to store unique elements.
    # Pros: Simple and efficient, operates in linear time.
    # Cons: Requires additional space proportional to the combined size of arr1 and arr2.
    dic = {}
    for i in arr1:
        dic[i] = True
    for j in arr2:
        dic[j] = True
    print(f"Count is: {len(dic)}")


union_using_dict([1, 32, 3, 24, 5], [1, 12, 3])
