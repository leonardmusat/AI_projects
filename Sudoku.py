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


def get_neighbors(row, column):
    neighbors = set()

    # get row
    for i in range(9):
        neighbors.add(matrix[i][column])

    # get column
    for i in range(9):
        neighbors.add(matrix[row][i])

    # get subgrid
    start_row = row - (row % 3)
    start_column = column - (column % 3)
    for i in range(3):
        for j in range(3):
            neighbors.add(matrix[start_row + i][start_column + j])

    neighbors.remove(matrix[row][column])

    return list(neighbors)


print(get_neighbors(6,4))


def generate_CSP(matrix):

    # create the variable list
    variables = [element for element in matrix]

    # create the domain for each variable in variables list
    domains = {var: [pos for pos in range(1, 10)] for var in variables}

    # find the neighbors for each variable
    neighbors = {var: get_neighbors(var) for var in variables}

    # create a CSP dictionary
    csp = {
        "variables": variables,
        "domains": domains,
        "neighbors": neighbors
    }

    for i in range(0, len(variables)-1):

        if i != 0:
            csp.get("domains")[i] = [variables[i]]  # pentru variabilele care au deja valoarea completata le schimb domeniul intr o lista doar cu acea variabila
        if  # aici vreau sa schimb si domeniul variabilelor care trebuie sa fie pare, le am declarat mai sus, even_variables,
            return csp


print(generate_CSP(matrix))