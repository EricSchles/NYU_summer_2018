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
    
    
def eq_float_solver(val, eq, epsilon=0.0001, step_size=0.001, debug=False):
    if abs(eq(val)) < epsilon:
        return round(val, 5)
    elif eq(val) > 0:
        if debug:
            val -= step_size
            result_one = eq_float_solver(val, eq)
            import code
            code.interact(local=locals())
            return result_one
        else:
            val -= step_size
            return eq_float_solver(val, eq)
    elif eq(val) < 0:
        if debug:
            val += step_size
            result_two = eq_float_solver(val, eq)
            import code
            code.interact(local=locals())
            return result_two
        else:
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
    

def arange(start, stop, step):
    cur = start
    while start < stop:
        yield cur
        cur += step
        
def iterative_solver(eq, start, stop, epsilon=0.0001, step_size=0.001):
    for val in arange(start, stop, step_size):
        if abs(eq(val)) < epsilon:
            return round(val, 5)

def iterative_diag_solver(eq, start, stop, epsilon=0.0001, step_size=0.001):
    for val in arange(start, stop, step_size):
        if abs(eq(val)) - 1 < epsilon:
            return round(val, 5)


def flatten(matrix):
    listing = []
    for row in matrix:
        for elem in row:
            listing.append(elem)
    return listing


def solve_matrix(matrix):
    flattened_matrix = flatten(matrix)
    largest_value = max(flattened_matrix)
    num_zeros = len(str(largest_value))
    val_range = int("1" + "0"*num_zeros)
    steps = []
    cur_matrix = matrix
    for index in range(len(matrix)):
        col_index = index
        row_index = index
        cur_matrix, step = solve_vector(cur_matrix[col_index][row_index],
                                        row_index, col_index, cur_matrix, val_range)
        steps.append(step)
    for row_index in range(len(matrix[0])):
        for col_index in range(len(matrix)):
            step = solve_vector(cur_matrix[col_index][row_index], 
                                row_index, col_index, cur_matrix, val_range)
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
    
    
def solve_vector(elem, cur_elem_idx, diag_index, matrix, magnitude):
    for row_index, matrix_row in enumerate(matrix):
        print(matrix)
        if cur_elem_idx == diag_index:
            equation = lambda elem, coef: elem/coef
            eq = partial(equation, elem)
            start, stop = magnitude*-1, magnitude

            reciprical = iterative_diag_solver(eq, start, stop)
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
    start, stop = magnitude*-1, magnitude
    coef = iterative_solver(to_solve, start=start, stop=stop)
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


#setrecursionlimit(10000)
if __name__ == '__main__':
    matrix = [[1, -2, 3], [1, 2, 1], [4, 2, 3]]
    steps = solve_matrix(matrix)
    apply_steps([3, 3, 7], steps)
