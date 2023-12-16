matrices = {
        1: [   [4,3,8],
                [9,5,1],
                [2,7,6]
            ],
        2: [
                [8,1,6],
                [3,5,7],
                [4,9,2]
            ],
        3: [
                [16, 3, 2,13],
                [ 5,10,11, 8],
                [ 9, 6, 7,12],
                [ 4,15,14, 1]
            ],
        4: [
                [16, 2, 3,13],
                [ 5,11,10, 8],
                [ 9, 7, 6,12],
                [ 4,14,15, 1]
            ],
        5: [
                [ 4,14,15, 1],
                [ 9, 7, 6,12],
                [ 5,11,10, 8],
                [16, 2, 3,13]
            ],
        6: [
                [17,24, 1, 8,15],
                [23, 5, 7,14,16],
                [ 4, 6,13,20,22],
                [10,12,19,21, 3],
                [11,18,25, 2, 9]
            ],
        7: [
                [64, 2, 3,61,60, 6, 7,57],
                [ 9,55,54,12,13,51,50,16],
                [17,47,46,20,21,43,42,24],
                [40,26,27,37,36,30,31,33],
                [32,34,35,29,28,38,39,25],
                [41,23,22,44,45,19,18,48],
                [49,15,14,52,53,11,10,56],
                [ 8,58,59, 5, 4,62,63, 1]
            ]
    }
        
def creator():
    len_ = ""
    while not len_.isdigit():
        len_ = input("Ingrese la longitud de la matriz: ")
    len_ = int(len_)
    empty_matrix = [[0 for _ in range(0, len_) ] for _ in range(0, len_)]
    # example = [0 for _ in range(0, 5)]
    return empty_matrix

def loader(empty_matrix):
    for row in range (len(empty_matrix)):
        for column in range(len(empty_matrix[row])):
            element = ""
            while not element.isdigit():
                element = input(f"{row},{column} Ingrese valor: ")
            element = int(element)
            empty_matrix[row][column] = element
    matrix = empty_matrix.copy()
    return matrix

def check(matrix):
    row_list = []
    for row in matrix:
        row_list.append(sum(row))
    print(row_list)
    print(matrix)

opcion = ""
while opcion not in ["L", "E", "1", "2", "3", "4", "5", "6", "7"]:
    opcion = input("Seleccione la opcion: ").upper()
    if opcion == "L":
        empty_matrix = creator()
        matrix = loader(empty_matrix)
        check(matrix)
    elif opcion in [str(n) for n in range(1,8)]:
        print(opcion)
        check(matrices[int(opcion)])
    else:
        exit()

