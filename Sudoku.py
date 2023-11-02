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

even_elements = [(2,2), (0,6), (2,8), (3,4), (4,3), (4,6), (4,5), (5,4), (0,6), (2,8), (6,6)]


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


def generate_dict(matrix):
    variables = [(i, j) for i in range(9) for j in range(9)]
    domains = {(i, j): [matrix[i][j]] if matrix[i][j] != 0 else (list(range(2, 10, 2)) if (i, j) in even_elements else list(range(1, 10))) for i, j in variables}
    neighbors = {var: get_neighbors(var) for var in variables}

    dict = {
        "variables": variables,
        "domains": domains,
        "neighbors": neighbors
    }

    return dict

dictionary = generate_dict(matrix)

def is_complete(matrix):
    for element in matrix:
        if element == 0:
            return False
    return True

def next_variable(matrix):
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                return row, col

def verify_update(var, value):  #doar verific daca se poate face mutarea
    for neighbor in get_neighbors(var):
        for element in dictionary["domain"][neighbor]:
            if (len(element) == 1 and element[0] == value):
                return False
    return True


def update_domains(var, value): #fac mutatrea propriu-zisa
    # var = tupla cu coordonatele variabilei, val = valoarea din domeniu care urmeaza sa fie luata
    for neighbor in get_neighbors(var):
        for element in dictionary["domain"][neighbor]:
            if (len(element) > 1 or  element[0] != value):
                dictionary["domain"][neighbor].remove(value)
    dictionary["domain"][var] = value
