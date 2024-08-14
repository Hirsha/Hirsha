import numpy as np

def main():
    # Define and initialize a 3x3 matrix
    matrix = np.array([[1.0, 1.0, 3.0],
                       [4.0, 5.0, -5.0],
                       [7.0, 8.0, 9.0]])

    # Compute the determinant
    det = np.linalg.det(matrix)

    # Print the determinant
    print(f"Determinant of the matrix is: {det}")

if __name__ == "__main__":
    main()