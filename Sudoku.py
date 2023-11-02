import copy

matrix = [
    [8,4,0,  0,5,0,  0,0,0],
    [3,0,0,  6,0,8,  0,4,0],
    [0,0,0,  4,0,9,  0,0,0],

    [0,2,3,  0,0,0,  9,8,0],
    [1,0,0,  0,0,0,  1,6,0],
    [0,9,8,  0,0,0,  1,6,0],

    [0,0,0,  5,0,4,  0,0,0],
    [0,3,0,  1,0,6,  0,0,7],
    [0,0,0,  0,2,0,  0,1,3]
]

even_elements = [(2,2), (0,6), (2,8), (3,4), (4,3), (4,5), (5,4), (0,6), (8,2), (6,6)]
#even_elements =[]

def get_neighbors(variable):
    row, col = variable
    neighbors = set()

    # Add neighbors in the same row
    for i in range(9):
        if i != col:
            neighbors.add((row, i))

    # Add neighbors in the same column
    for i in range(9):
        if i != row:
            neighbors.add((i, col))

    # Add neighbors in the same 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if (i, j) != variable:
                neighbors.add((i, j))

    return list(neighbors)


#print(get_neighbors(a))


def generate_dict(matrix, even_elements):
    variables = [(i, j) for i in range(9) for j in range(9)]
    neighbors = {var: get_neighbors(var) for var in variables}

    def get_domain(i, j):
        if matrix[i][j] != 0:
            return [matrix[i][j]]

        domain = set(range(1, 10))

        # Exclude values present in the same row and column
        for k in range(9):
            if matrix[i][k] != 0:
                domain.discard(matrix[i][k])
            if matrix[k][j] != 0:
                domain.discard(matrix[k][j])

        # Exclude values present in the same 3x3 subgrid
        subgrid_i, subgrid_j = i // 3, j // 3
        for x in range(subgrid_i * 3, subgrid_i * 3 + 3):
            for y in range(subgrid_j * 3, subgrid_j * 3 + 3):
                if matrix[x][y] != 0:
                    domain.discard(matrix[x][y])

        # If the variable is in even_elements, restrict to even values
        if (i, j) in even_elements:
            domain = set(val for val in domain if val % 2 == 0)

        return list(domain)

    domains = {(i, j): get_domain(i, j) for i, j in variables}

    return {
        "variables": variables,
        "domains": domains,
        "neighbors": neighbors
    }

#dictionary = generate_dict(matrix)
#print(dictionary)


def is_complete(matrix):
    for row in matrix:
        if 0 in row:
            return False

    for i in range(9):
        if len(set(matrix[i])) != 9:
            return False

        column = [matrix[j][i] for j in range(9)]
        if len(set(column)) != 9:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [matrix[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subgrid)) != 9:
                return False

    return True


def next_variable(dict_new, matrix):
    min_domain_size = 10
    result = 0

    for var in dict_new["variables"]:
        if matrix[var[0]][var[1]] == 0 and len(dict_new["domains"][var]) < min_domain_size:
            min_domain_size = len(dict_new["domains"][var])
            result = var
    return result



def verify_update(var, value, dict_new):  #doar verific daca se poate face mutarea
    for neighbor in get_neighbors(var):
        if len(dict_new["domains"][neighbor]) == 1:
            if dict_new["domains"][neighbor][0] == value:
                return False
    return True


def update_matrix(var, value, matrix): #fac mutatrea propriu-zisa
    # for neighbor in get_neighbors(var):
    #     for element in dict_new["domains"][neighbor]:
    #         if len(dict_new["domains"][neighbor]) > 1 or element != value:
    #             if value in dict_new["domains"][neighbor]:
    #                 dict_new["domains"][neighbor].remove(value)
    # dict_new["domains"][var] = [value]
    matrix_temp = copy.deepcopy(matrix)
    matrix_temp[var[0]][var[1]] = value
    return matrix_temp


def Forward_checking(matrix):
    if is_complete(matrix):
        return matrix

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print()


    dict_new = generate_dict(matrix, even_elements)
    var = next_variable(dict_new, matrix)
    #print(dict_new["domains"][var])

    print(var, ": ", dict_new["domains"][var])
    print()
    for neighbor in get_neighbors(var):
        print(neighbor,": ", dict_new["domains"][neighbor])
    print()

    for value in dict_new["domains"][var]:
        if verify_update(var, value, dict_new):
            matrix1 = update_matrix(var, value, matrix)
            matrix_final = Forward_checking(matrix1)
            if matrix_final != 0:
                return matrix_final
    return 0


matrix_done = Forward_checking(matrix)
if (matrix_done != 0):
    for row in matrix_done:
        for element in row:
            print(element, end=" ")
        print()
else:
    print(0)