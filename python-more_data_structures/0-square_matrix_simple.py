#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nm = []
    for vec in matrix:
        sqr_vec = []
        for i in vec:
            sqr_vec.append(i**2)
        nm.append(sqr_vec)
    return(nm)