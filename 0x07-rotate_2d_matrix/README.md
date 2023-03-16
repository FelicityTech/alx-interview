# Rotate 2D Matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

	Prototype: def rotate_2d_matrix(matrix):
	Do not return anything. The matrix must be edited in-place.
	You can assume the matrix will have 2 dimensions and will not be empty.



To rotate a 2D matrix 90 degrees clockwise, we need to transpose the matrix (swap the rows and columns) and then reverse each row of the transposed matrix. We can perform this operation in place by swapping elements of the matrix.

Here's a step-by-step explanation of the algorithm:
1. Transpose the matrix by swapping each element (i, j) with element (j, i), where i and j are indices of the matrix. This can be done with a nested loop over the upper triangle of the matrix (i.e., i < j).

2. Reverse each row of the transposed matrix. This can be done with a loop over the rows of the matrix, swapping the elements on opposite sides of the row.
