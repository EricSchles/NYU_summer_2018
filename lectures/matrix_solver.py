from functools import partial
from random import random
from sys import setrecursionlimit

def eq_solver(val, func):
    if func(val) > 0:
        val -= 1
        return eq_solver(val, func)
    elif func(val) < 0:
        val += 1
        return eq_solver(val, func)
    else:
        return round(val, 5)
    
    
def eq_float_solver(val, eq, epsilon=0.0001, step_size=0.001):
    if abs(eq(val)) < epsilon:
        print("got here")
        return round(val, 5)
    elif eq(val) > 0:
        val -= step_size
        return eq_float_solver(val, eq)
    elif eq(val) < 0:
        val += step_size
        return eq_float_solver(val, eq)
    else:
        return round(val, 5)


def eq_diag_solver(val, eq, epsilon=0.0001, step_size=0.001):
    if abs(eq(val)) - 1 < epsilon:
        print("got here with val", val)
        return round(val, 5)
    elif eq(val) > 1:
        val -= step_size
        if val == 0:
            val -= step_size
        return eq_float_solver(val, eq)
    elif eq(val) < 1:
        val += step_size
        if val == 0:
            val += step_size
        return eq_float_solver(val, eq)
    else:
        return round(val, 5)
    
    
def solve_matrix(matrix):
    steps = []
    cur_matrix = matrix
    for index, row in enumerate(matrix):
        for cur_elem_idx in range(len(row)):
            if index == cur_elem_idx:
                cur_matrix, step = solve_vector(cur_matrix[index][cur_elem_idx],
                                          cur_elem_idx, index, cur_matrix)
            else:
                step = solve_vector(cur_matrix[index][cur_elem_idx], 
                                    cur_elem_idx, index, cur_matrix)
                cur_matrix = linear_combination(cur_matrix, step)
            steps.append(step)
    return steps


def linear_combination(matrix, step):
    update_row = step[0]
    other_row = step[1]
    transformer = step[2]
    for index in range(len(matrix[0])):
        matrix[update_row][index] = transformer(
            matrix[update_row][index], matrix[other_row][index])
    return matrix
    
    
def solve_vector(elem, cur_elem_idx, diag_index, matrix):
    for row_index, matrix_row in enumerate(matrix):
        print(matrix)
        if cur_elem_idx == diag_index:
            equation = lambda elem, coef: elem/coef
            eq = partial(equation, elem)
            reciprical = eq_diag_solver(1, eq)
            matrix[diag_index] = [elem*reciprical 
                                  for elem in matrix[diag_index]]
            operation = lambda coef, elem: elem*coef
            op = partial(operation, reciprical)
            step = [diag_index, cur_elem_idx, op, None, reciprical, "rescale"]
            return matrix, step
        if matrix_row[cur_elem_idx] != 0 and row_index != diag_index:
            other_elem = matrix_row[cur_elem_idx]
            other_row = row_index
            break
    eq_to_solve = lambda elem, other_elem, coef: elem + coef*other_elem
    to_solve = partial(eq_to_solve, elem, other_elem)
    try:
        coef = eq_float_solver(0, to_solve)
    except:
        import code
        code.interact(local=locals())
    operation = lambda coef, elem, other: elem + coef*other
    op = partial(operation, coef)
    return [diag_index, cur_elem_idx, op, other_row, coef, "linear_combo"]


def apply_steps(vector, steps):
    for step in steps:
        if step[-1] == "linear_combo":
            idx = step[0]
            other_idx = step[3]
            coef = step[4]
            vector[idx] = vector[idx] + coef*vector[other_idx]
        else:
            idx = step[0]
            coef = step[4]
            vector[idx] = vector[idx]*coef
    return vector

setrecursionlimit(10000)
matrix = [[1, -2, 3], [1, 2, 1], [4, 2, 3]]
steps = solve_matrix(matrix)
apply_steps([3, 3, 7], steps)
