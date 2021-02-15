import time


def init(params):
    matrix = []
    for column in range(0, params["column"]):
        matrix.append([0 for row in range(0, params["row"])])
    return matrix


def get_column(params):
    column = None
    valid = False
    while (not valid):
        try:
            column = int(
                input(f"Choice column between 1 and {params['column']} : "))
            if 1 <= column <= params["column"]:
                valid = True
        except ValueError:
            pass
    return column - 1


def show(params, matrix):
    emoji = ["⚪️", "🔵", "🔴"]
    for row in reversed(range(0, params["row"])):
        for column in range(0, params["column"]):
            number = matrix[column][row]
            print(emoji[number], end=' ')
        print()


def win(matrix, pawn):
    value = [0, 1, 2, 3]

    # Vertical
    for row in range(0, params["row"]):
        for column in range(0, params["column"] - 3):
            temp = True
            cpt = 0
            for v in value:
                if (row + v) < params["row"]:
                    if (matrix[column][row + v] != pawn):
                        temp = False
                    cpt += 1
            if temp and cpt == 4:
                return "gagné"

    # Horizontal
    for column in range(0, params["column"] - 3):
        for row in range(0, params["row"]):
            temp = True
            cpt = 0
            for v in value:
                if (column + v) < params["column"]:
                    if (matrix[column + v][row] != pawn):
                        temp = False
                    cpt += 1
            if temp and cpt == 4:
                return "gagné"

    # Positive diagonal
    for column in range(0, params["column"] - 3):
        for row in range(0, params["row"] - 3):
            temp = True
            cpt = 0
            for v in value:
                if (column + v) < params["column"] and (row + v) < params["row"]:
                    if (matrix[column + v][row + v] != pawn):
                        temp = False
                    cpt += 1
            if temp and cpt == 4:
                return "gagné"

    # Negative diagonal
    for column in range(0, params["column"] - 3):
        for row in range(0, params["row"]):
            temp = True
            cpt = 0
            for v in value:
                if (column + v) < params["column"] and (row + v) < params["row"]:
                    if (matrix[column - v][row + v] != pawn):
                        temp = False
                    cpt += 1
            if temp and cpt == 4:
                return "gagné"

    # Partie nulle
    cpt = 0
    for column in matrix:
        if 0 not in column:
            cpt += 1

    if cpt == params["column"]:
        return "nulle"

    return False


def minimax():
    return 0


def run(params, matrix):
    stop = False

    joueur = 2
    while (not stop):
        if joueur == 1:
            joueur = 2
        elif joueur == 2:
            joueur = 1

        show(params, matrix)
        print(f"Joueur {joueur}")
        column = get_column(params)
        try:
            y = matrix[column].index(0)
            matrix[column][y] = joueur

            # Partie nulle
            if (win(matrix, joueur) == "nulle"):
                stop = True
                print("\n\nPartie nulle")
                show(params, matrix)

            if (win(matrix, joueur) == "gagné"):
                stop = True
                print(f"\n\nVictoire du joueur {joueur}")
                show(params, matrix)
        except ValueError:
            pass


def autorun(params, matrix):
    stop = False

    pNull = [
        1, 3, 2, 4, 4, 1, 3, 6, 5, 2, 2, 6, 7, 5, 2, 4, 7, 7, 7, 7, 1, 3, 3, 1,
        2, 3, 3, 1, 4, 6, 6, 7, 5, 2, 6, 4, 4, 6, 1, 5, 5, 5
    ]

    pLigne = [
        1, 2, 2, 3, 3, 4, 3, 4, 4, 5
    ]

    pDiagonale = [
        1, 2, 2, 3, 3, 4, 3, 4, 4, 6, 4
    ]

    pColumn = [
        1, 2, 1, 2, 1, 2, 1
    ]

    joueur = 2
    for column in pNull:
        time.sleep(0.25)
        if joueur == 1:
            joueur = 2
        elif joueur == 2:
            joueur = 1

        show(params, matrix)
        print(f"Joueur {joueur}")
        print(f"Choice column between 1 and {params['column']} : {column}")
        column -= 1
        y = matrix[column].index(0)
        matrix[column][y] = joueur

        # Partie nulle
        if (win(matrix, joueur) == "nulle"):
            stop = True
            print("\n\nPartie nulle")
            show(params, matrix)

        if (win(matrix, joueur) == "gagné"):
            stop = True
            print(f"\n\nVictoire du joueur {joueur}")
            show(params, matrix)


if __name__ == "__main__":
    params = {"column": 7, "row": 6}
    matrix = init(params)
    #run(params, matrix)
    autorun(params, matrix)
