array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_matrix(arr):
    # Prints the elements of a given matrix.

    # Time Complexity: O(n), where n is the total number of elements in the matrix.
    # Auxiliary Space Complexity: O(1) (not counting the input matrix).
    # Pros: Simple function to visually display a matrix.
    # Cons: None specific to the function itself; may become inefficient for very large matrices due to console output size.
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(f"{arr[i][j]} ", end=" ")
        print("\n")


print_matrix(array)

# Addition of matrix
# First array:
# 1 2 3
# 4 5 6
# 6 7 8
# Second array:
# 9 8 7
# 6 5 4
# 3 2 1
# Addition:
# 10 10 10
# 10 10 10
# 10 10 10

array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


def addition_of_matrix(arr1, arr2):
    # Adds two matrices element-wise and prints the resulting matrix.

    # Time Complexity: O(n), where n is the total number of elements in the matrices.
    # Auxiliary Space Complexity: O(n), as it requires extra space to store the resulting matrix.
    # Pros: Performs straightforward addition of matrices.
    # Cons: Requires both input matrices to have the same dimensions.
    sumOfmatrix = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[i])):
            row.append(arr1[i][j] + arr2[i][j])

        sumOfmatrix.append(row)
    print_matrix(sumOfmatrix)


addition_of_matrix(array1, array2)


def search_in_sorted_matrix(arr):
    # Searches for a value in a sorted matrix and prints its position if found.

    # Time Complexity: O(n), where n is the total number of elements in the matrix.
    # Auxiliary Space Complexity: O(1).
    # Pros: Optimized for sorted matrices, efficiently finds the target value.
    # Cons: Requires the matrix to be sorted; performs a simple linear search which might not be optimal for very large matrices.
    search = 3
    found = False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == search:
                found = True
                print(f"value: {search} found in row: {i+1} column: {j+1}")
    if found == False:
        print(f"Not found value: {search}")


search_in_sorted_matrix(array2)
