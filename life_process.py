import numpy as np
from seeds import SEED


def generation(field):
    """
    This function creates one iteration of game

    :param field: numpy.ndarray (represents current state)
    :return: numpy.ndarray (new state)
    """
    new = np.copy(field)

    for y in range(field.shape[0]):
        for x in range(field.shape[1]):
            new[y, x] = rules(x, y, field)
    return new


def rules(x, y, field):
    """
    Determine survival for a specific cell according to original rules.
    Calculations simulate an infinite universe.

    :param x: int (horizontal position)
    :param y: int (vertical position)
    :param field: numpy.ndarray (represents current state)
    :return:
    """
    # get field size for math
    ny = field.shape[0]
    nx = field.shape[1]

    # count 8 neighbors
    num_neighbors = int((field[y, (x - 1) % nx] + field[y, (x + 1) % nx] +
                         field[(y - 1) % ny, x] + field[(y + 1) % ny, x] +
                         field[(y - 1) % ny, (x - 1) % nx] + field[(y - 1) % ny, (x + 1) % nx] +
                         field[(y + 1) % ny, (x - 1) % nx] + field[(y + 1) % ny, (x + 1) % nx]))

    # apply rules
    if field[y, x] and not 2 <= num_neighbors <= 3:
        return 0
    elif num_neighbors == 3:
        return 1
    return field[y, x]


def place(field, seed, point):
    """
    Generate a universe of a given size and populate with a starter seed.

    :param field:numpy.ndarray (represents current state)
    :param seed: str (name for the seed array)
    :param point:str (tuple of integers representing the start point)
    """

    # initialize start point
    x_p, y_p = point

    # get field size for math
    nx = field.shape[1]
    ny = field.shape[0]

    # determine where to place top left corner
    i = x_p - int(seed.shape[1] / 2)
    j = y_p - int(seed.shape[0] / 2)

    # place seed (top left corner at x, y)
    for y in range(seed.shape[0]):
        for x in range(seed.shape[1]):
            field[(j + y) % ny, (i + x) % nx] = seed[y, x]

    return field


def seeded_field(field_size, start_seed, start_seed_point):
    """
    Generate field of a given size and populate with a starter seed.

    :param field_size: tuple
    :param start_seed: str (name for a seed array)
    :param start_seed_point: str (tuple of integers representing the start seed position)
    """
    field = np.zeros((field_size[1], field_size[0]))

    # set desired seed
    seed = SEED["infinite"]
    if start_seed in SEED.keys():
        seed = SEED[start_seed]

    # approx midpoint of the universe (x, y)
    if start_seed_point[0] < 0 or start_seed_point[1] < 0:
        point = (int(field.shape[1] / 2), int(field.shape[0] / 2))
    else:
        point = start_seed_point

    # seed the universe
    field = place(field, seed, point)

    return field
