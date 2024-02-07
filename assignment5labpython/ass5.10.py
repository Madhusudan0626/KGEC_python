def multiply_matrices(matrix1, matrix2):
    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied. Invalid dimensions.")
        return None

    # Initialize a result matrix with zeros
    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

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

# Call the function to multiply matrices
result_matrix = multiply_matrices(matrix_a, matrix_b)

# Print the result matrix
if result_matrix:
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
