#!/usr/bin/python3

def matrix_divided(matrix, div):
    for lst in matrix:
        for num in lst:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix =[]
    for lst in matrix:
        new_lst = []
        new_matrix.append(new_lst)
        for x in range(len(lst)):
            k = lst[x] / div
            rounded_k = round(k, 2)
            new_lst.append(rounded_k)

    return (new_matrix)
