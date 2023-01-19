def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # grab from each list an increasing index, 0,1,2, etc... while lower than list length
    # while loop?
    # but then do the same thing backwards.
    # can use negative indexing [-1] is the last element in the list
    # add em up and return the sum/
    # add as you go, actually

    total = 0
    for x in range(len(matrix)):
        total += matrix[x][x]
        total += matrix[x][-1 - 1]

    return total

    # not exactly sure about the second line, [-1 - 1], how that selects the right index...

    
