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

if __name__ == "__main__":
    main()