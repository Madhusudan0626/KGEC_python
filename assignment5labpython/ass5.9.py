def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None

    # Initialize a result matrix with zeros
    result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Perform matrix addition
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix

# Example matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Call the function to add matrices
result_matrix = add_matrices(matrix_a, matrix_b)

# Print the result matrix
if result_matrix:
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
