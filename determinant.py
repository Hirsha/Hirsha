from matplotlib.pylab import rand
import numpy as np

def main():
    # Define and initialize a 3x3 matrix
    matrix = np.array([[rand(), rand(), rand()],
                       [rand(), rand(), rand()],
                       [rand(), rand(), rand()]])

    # Compute the determinant
    det = np.linalg.det(matrix)

    print(matrix)

    # Print the determinant
    print(f"Determinant of the matrix is: {det}")

    matrix2 = np.full((2, 2, 2), 4)
    print(matrix2)
    det2 = np.linalg.det(matrix2)
    print(f"Determinant of the matrix is: {det2}")

    matrix3 = np.array([[[1,2],[1,2]],[[1,2],[1,2]]])
    print(matrix3)

if __name__ == "__main__":
    main()