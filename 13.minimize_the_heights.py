def defferenceOfHeight(arr, k):
    # Computes the minimum possible difference between the heights of the tallest and shortest
    # towers after either adding or subtracting k from each tower's height.
    # Time Complexity: O(n log n) due to sorting
    # Space Complexity: O(1) since only a constant amount of extra space is used.
    # Pros: Efficient approach leveraging sorting and a linear scan to find the optimal solution.
    # Cons: Requires sorting, which might not be necessary in some cases if the array is already sorted.
    n = len(arr)
    if n == 0:
        return 0
    arr.sort()
    ans = arr[n - 1] - arr[0]
    small = arr[0] + k
    large = arr[n - 1] - k
    if small > large:
        large, small = small, large

    for i in range(1, n - 1):
        sub = arr[i] - k
        add = arr[i] + k
        if sub >= small or add <= large:
            continue
        if large - sub <= add - sub:
            small = sub
        else:
            large = add

    return min(ans, large - small)


print(defferenceOfHeight([3, 9, 12, 16, 20], 3))


def bruteForceMinDiff(arr, k):
    # Computes the minimum possible difference between the heights of the tallest and shortest
    # towers after either adding or subtracting k from each tower's height using a brute-force
    # recursive approach.
    # Time Complexity: Exponential, O(2^n), as each element can be either increased or decreased.
    # Space Complexity: O(n) due to the recursive stack, where n is the length of the array.
    # Pros: Provides a straightforward approach to explore all possible combinations.
    # Cons: Very inefficient for large arrays due to exponential time complexity.
    n = len(arr)

    def recurse(index, currnetArr):
        if index == n:
            return max(currnetArr) - min(currnetArr)

        currnetArr[index] += k
        incDiff = recurse(index + 1, currnetArr)
        currnetArr[index] -= k

        currnetArr[index] -= k
        decDiff = recurse(index + 1, currnetArr)
        currnetArr[index] += k

        return min(incDiff, decDiff)

    return recurse(0, arr[:])


print(bruteForceMinDiff([3, 9, 12, 16, 20], 3))
