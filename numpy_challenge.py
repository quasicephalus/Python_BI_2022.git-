import numpy as np

# 3 different ways to create array:
if __name__ == "__main__":
    list = ['rubor', 'tumor', 'calor', 'dolor', 'functio laesa']
    # This is an iflammated array
    method1 = np.array(list)
    # From one to lucky
    method2 = np.arange(1, 14)
    # True array
    method3 = np.ones(1, dtype=bool)


# God bless numpy!
def matrix_multiplication(mat1, mat2):
    return np.matmul(mat1, mat2)


def multiplication_check(mat_list):
    # I'm not shure if the list is always correct, so it's better to check.
    if len(mat_list) < 2:
        return False

    # For probable optimisation, working with matrix sizes, not matrices themselves.
    # It is a recursive function.
    def shape_check(shapes):
        # We need to check if number of columns in first matrix is  equal to number of rows in second one.
        cols = shapes[0][1]
        rows = shapes[1][0]
        # Recursion base is the list with 2 matrices.
        if len(shapes) == 2:
            return cols == rows
        # For larger lists, checking first two matrices, and if they're multipliable, continue.
        if cols == rows:
            # Second matrix is now multiplied by first, and first is removed.
            shapes[1] = (rows, cols)
            shapes.remove(shapes[0])
            return shape_check(shapes)
        # On every step, if next matrix is not multipliable by previous, return False.
        else:
            return False

    # Getting sizes
    shapes = [np.shape(mat) for mat in mat_list]
    return shape_check(shapes)


# Multiplying matrices in the same recursive way as checking
def multiply_matrices(mat_list):
    if multiplication_check(mat_list):
        # return np.linalg.multi_dot(mat_list)
        if len(mat_list) == 2:
            return np.matmul(mat_list[0], mat_list[1])
        # Second matrix is multiplied by first, first removed.
        mat_list[1] = np.matmul(mat_list[0], mat_list[1])
        mat_list.remove(mat_list[0])
        return multiply_matrices(mat_list)


# Vector length is a norm of vector, and numpy has function for that.
def compute_2d_distance(a, b):
    return np.linalg.norm(a - b)


# Vector could be of any dimensions.
def compute_multidimensional_distance(a, b):
    return np.linalg.norm(a - b)


# TOTAL PAIN!
# Idea of creating the new matrix with a function is pretty obvious, but it doesn't seem to work the way I thought.
# Initially I have just wrote "lambda i, j: np.linalg.norm(array[i] - array[j]"
# and expected it just to put required value in distances[i,j],
# but "distances" was just float number, not an array with "size" shape.
# The solution was to use axis argument, which is totally not understood.
# Is it so because in np.fromfunction shape of final array is determined by shape of used function output?
def compute_pair_distances(array):
    size = (np.shape(array)[0], np.shape(array)[0])
    distances = np.fromfunction(
        lambda i, j: np.linalg.norm(array[i] - array[j], axis=2),
        size, dtype=int)
    return distances
