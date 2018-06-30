from functools import partial

def eq_solver(val, func):
    if func(val) == 0:
        return val
    if func(val) > 0:
        val -= 1
        return eq_solver(val, func)
    elif func(val) < 0:
        val += 1
        return eq_solver(val, func)


def eq_solver2(func):
    for i in range(-100, 100):
        if func(i) == 0:
            return i
        
def solve_matrix(matrix):
    steps = []
    cur_matrix = matrix
    for index, row in enumerate(matrix):
        for cur_elem_idx, elem in enumerate(row):
            step = solve_vector(elem, cur_elem_idx, index, cur_matrix)
            if step[3] == "row_combine":
                cur_matrix = linear_combination(cur_matrix, step)
            steps.append(step)
    return steps


def linear_combination(matrix, step):
    update_row = step[0]
    other_row = step[1]
    transformer = step[2]
    for index in range(len(matrix[0])):
        try:
            matrix[update_row][index] = transformer(
                matrix[update_row][index], matrix[other_row][index]
            )
        except:
            import code
            code.interact(local=locals())

    return matrix


def solve_vector(elem, cur_elem_idx, diag_index, matrix):
    for row_index, matrix_row in enumerate(matrix):
        if row_index == diag_index:
            continue
        if matrix_row[cur_elem_idx] != 0:
            other_elem = matrix_row[cur_elem_idx]
            other_row = row_index
    solve_for_coef = lambda elem, other, coef: elem + coef*other
    to_solve = partial(solve_for_coef, elem, other_elem)
    #coef = eq_solver(0, to_solve)
    coef = eq_solver2(to_solve)
    operation = lambda coef, elem, other: elem + coef*other
    if coef is None:
        import code
        code.interact(local=locals())
    op = partial(operation, coef)
    return [diag_index, other_row, op, "row_combine"]


def apply_steps(vector, steps):
    return vector


matrix = [[1, -2], [1, 2]]
print(solve_matrix(matrix))
