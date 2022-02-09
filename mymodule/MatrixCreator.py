# !/usr/bin/pyhon
import numpy as np
import random


def GetMeMatrix(n, k):
    """This is a function, that create Array of random elements

    Args:
        n (int): "width" of Array
        k (int): "height" of Array
    """
    random.seed(version=2)
    # array = np.random.randint(0, 100, size=(n, k), dtype=int)
    array = [[random.randrange(0, 100, 1) for _ in range(n)] for i in range(k)]
    return array
