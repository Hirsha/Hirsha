#include <stdio.h>

double determinant3x3(double matrix[3][3]) {
    double det;

    // Calculate the determinant of a 3x3 matrix using the rule of Sarrus
    det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
          matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
          matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);

    return det;
}

int main() {
    // Define and initialize a 3x3 matrix
    double matrix[3][3] = {
        {1.0, 2.0, 3.0},
        {4.0, 5.0, 6.0},
        {7.0, 8.0, 9.0}
    };

    // Compute the determinant
    double det = determinant3x3(matrix);

    // Print the determinant
    printf("Determinant of the matrix is: %f\n", det);

    return 0;
}
