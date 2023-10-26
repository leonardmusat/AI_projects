def matrix_init(lst):
    matrix = [[{} for _ in range(3)] for _ in range(3)]

    if len(lst) != 9:
        print("The list with numbers does not contain 9 numbers.")
    if all(item in lst for item in range(9)) == 0:
        print("The list should contain the number from 0 to 8")

    for i in range(3):
        for j in range(3):
            matrix[i][j] = {lst[i * 3 + j]: 0}  # populez matricea cu dictioinare care au cheia nr de la 0 la 8 si valoarea 0
    return matrix



def validate_final(matrix):

    counter = 0

    if matrix == 0 or matrix == 1:
        return False

    for row in matrix:
        for cell in row:
            if list(cell.keys())[0] == counter:
                counter = counter + 1  # validez matricea de final, trebuie sa aiba keile dictionarelor in ordine crecatoare
            else:
                return False
    if counter == 9:
        return True

    return False


def find_zero(matrix):

    rez = []

    for i in range(3):
        for j in range(3):
            mat = list(matrix[i][j].keys())[0]
            if mat == 0:
                rez.append(i)
                rez.append(j)

    return rez


arr = [int(i) for i in input().split()] #citim un prim array de la tastatura
matrix = matrix_init(arr)
print(matrix)
print(find_zero(matrix))
coord_list = []
coord_list = coord_list + find_zero(matrix)
#list_of_moves = ['up', 'down', 'left', 'right']
#(validate_final(matrix))


def get_validate_neighbors(matrix, row, col):

    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    neighbors_offsets = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    neighbors = []
    for offset_row, offset_col in neighbors_offsets:
        neighbor_row = row + offset_row
        neighbor_col = col + offset_col
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols: #validate the neighbors
            neighbors.append(matrix[neighbor_row][neighbor_col])

    return neighbors


def validate_cell(row, col):
    if 0 <= row <= 2 and 0 <= col <= 2:
        return False
    else:
        return True

def validate_move (matrix, row, col):

    if matrix == 0 or matrix == 1:
        return False

    if list(matrix[row][col].values())[0] == 0:
        return True

    else:
        return False



def compute_transition_up(matrix, string):

    if string == 'up':
        row1, col1 = coord_list
        row2 = row1-1

        if validate_cell(row2, col1):
            return 0

        if validate_move(matrix, row2, col1):

            matrix[row1][col1] = matrix[row2][col1]
            matrix[row2][col1] = {0: 0}

            coord_list[0] = row2
            coord_list[1] = col1

            neighbors_to_unlock = get_validate_neighbors(matrix, row2, col1)
            for dict in neighbors_to_unlock:
                key = list(dict.keys())[0]
                dict[key] = 0

            key = list(matrix[row1][col1].keys())[0]
            matrix[row1][col1][key] = 1

        else:
            return 1

    return matrix


def compute_transition_down(matrix, string):

    if string == 'down':

        row1, col1 = coord_list
        row2 = row1 + 1

        if validate_cell(row2, col1):
            return 0

        if validate_move(matrix, row2, col1):

            matrix[row1][col1] = matrix[row2][col1]
            matrix[row2][col1] = {0: 0}

            coord_list[0] = row2
            coord_list[1] = col1

            neighbors_to_unlock = get_validate_neighbors(matrix, row2, col1)
            for dict in neighbors_to_unlock:
                key = list(dict.keys())[0]
                dict[key] = 0

            key = list(matrix[row1][col1].keys())[0]
            matrix[row1][col1][key] = 1

        else:
            return 1

    return matrix


def compute_transition_right(matrix, string):

    if string == 'right':

        row1, col1 = coord_list
        col2 = col1 + 1

        if validate_cell(row1, col2):
            return 0

        if validate_move(matrix, row1, col2):

            matrix[row1][col1] = matrix[row1][col2]
            matrix[row1][col2] = {0: 0}

            coord_list[0] = row1
            coord_list[1] = col2

            neighbors_to_unlock = get_validate_neighbors(matrix, row1, col2)
            for dict in neighbors_to_unlock:
                key = list(dict.keys())[0]
                dict[key] = 0

            key = list(matrix[row1][col1].keys())[0]
            matrix[row1][col1][key] = 1

        else:
            return 1

    return matrix


def compute_transition_left(matrix, string):

    if string == 'left':

        row1, col1 = coord_list
        col2 = col1 - 1

        if validate_cell(row1, col2):
            return 0

        if validate_move(matrix, row1, col2):

            matrix[row1][col1] = matrix[row1][col2]
            matrix[row1][col2] = {0: 0}

            coord_list[0] = row1
            coord_list[1] = col2

            neighbors_to_unlock = get_validate_neighbors(matrix, row1, col2)
            for dict in neighbors_to_unlock:
                key = list(dict.keys())[0]
                dict[key] = 0

            key = list(matrix[row1][col1].keys())[0]
            matrix[row1][col1][key] = 1

        else:
            return 1

    return matrix


# print(compute_transition_down(matrix, "down"))
# print(compute_transition_up(matrix, "up"))
# print(compute_transition_right(matrix, "right"))


def IDDFS(matrix, max_depth):
    for limit in range (0, max_depth):
           if DLS(matrix, limit) == True:
                return True
    return False

def DLS(matrix, limit):

    if validate_final(matrix):
        return True

    if (limit <= 0):
        return False

    for index in range (0, limit):

        matrix1 = compute_transition_up(matrix, 'up')
        if (matrix1 != 1 and matrix1 != 0):
            print(matrix1, 'up')
            if DLS(matrix1, limit-1):
                return True

        matrix2 = compute_transition_down(matrix, 'down')
        if (matrix2 != 1 and matrix2 != 0):
            print(matrix2, 'down')
            if DLS(matrix2, limit - 1):
                return True

        matrix3 = compute_transition_right(matrix, 'right')
        if (matrix3 != 1 and matrix3 != 0):
            print(matrix3, 'right')
            if DLS(matrix3, limit - 1):
                return True

        matrix4 = compute_transition_left(matrix, 'left')
        if (matrix4 != 1 and matrix4 != 0):
            print(matrix4, 'left')
            if DLS(matrix4, limit-1):
                return True


    return False


print(IDDFS(matrix, 3))
# print(validate_final(matrix))