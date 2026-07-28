# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed 
def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0]) if rows > 0 else 0
    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0
    
    if cols_a != rows_b:
        raise ValueError("Number of columns in A must equal number of rows in B.")
    
    result = [[0] * cols_b for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:>5}" for val in row))

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                row = list(map(int, row_input.split()))
                if len(row) != cols:
                    print(f"Please enter exactly {cols} values.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter integers only.")
    return matrix

def main():
    print("=== Part A: Transpose a Matrix ===")
    rows_a = int(input("Enter number of rows for matrix A: "))
    cols_a = int(input("Enter number of columns for matrix A: "))
    matrix_a = read_matrix(rows_a, cols_a)

    print("\nOriginal Matrix A:")
    print_matrix(matrix_a)

    transposed_a = transpose_matrix(matrix_a)
    print("\nTransposed Matrix A:")
    print_matrix(transposed_a)

    print("\n=== Part B: Add Two Matrices ===")
    
    rows_b = int(input("Enter number of rows for matrix B: "))
    cols_b = int(input("Enter number of columns for matrix B: "))
    matrix_b = read_matrix(rows_b, cols_b)

    rows_t = int(input("Enter number of rows for matrix B: "))
    cols_t = int(input("Enter number of columns for matrix B: "))
    matrix_t = read_matrix(rows_t, cols_t)

    if rows_b != rows_t or cols_b != cols_t:
        print("Error: Matrices must be of the same size for addition.")
    else:
        sum_matrix = add_matrices(matrix_b, matrix_t)
        print("\nMatrix A + Matrix B:")
        print_matrix(sum_matrix)

    print("\n=== Part C: Multiply Two Matrices ===")
    rows_c = int(input("Enter number of rows for matrix A: "))
    cols_c = int(input("Enter number of columns for matrix A: "))
    matrix_c = read_matrix(rows_c, cols_c)

    rows_d = int(input("Enter number of rows for matrix B: "))
    cols_d = int(input("Enter number of columns for matrix B: "))
    matrix_d = read_matrix(rows_d, cols_d)

    if cols_c != rows_d:
        print("Error: Number of columns in A must equal number of rows in B.")
    else:
        product_matrix = multiply_matrices(matrix_c, matrix_d)
        print("\nMatrix A x Matrix B:")
        print_matrix(product_matrix)


if __name__ == "__main__":
    main()