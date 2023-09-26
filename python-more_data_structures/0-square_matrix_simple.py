def square_matrix_simple(matrix=[]):
    nm = []
    for vec in matrix:
        sqr_vec = []
        for i in vec:
            sqr_vec.append(i**2)
        nm.append(sqr_vec)

    return(nm)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)