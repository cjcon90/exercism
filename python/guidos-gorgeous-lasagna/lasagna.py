"""
Solution to Guido's Gorgeous Lasagna
https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time:int) -> int:
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers:int) -> int:
    '''
    :param layers: int how many layers to use in lasagna
    :return: int total time to prepare selected number of layers

    function that takes how many layers chef wishes to user in lasagna
    and returns how many minutes it will take to prepare, based on the
    'PREPARATION_TIME' per layer
    '''

    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers:int, elapsed_bake_time:int) -> int:
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :param layers: int how many layers to use in lasagna

    function that returns how much time has elapsed when combining
    the current elapsed cooking time, and the preparation time,
    based on the function 'preparation_time_in_minutes()'
    '''

    return elapsed_bake_time + preparation_time_in_minutes(layers)
