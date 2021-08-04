import matplotlib.pyplot as plt
import numpy as np
import time


def grid():

    chessboard = np.zeros((6, 6))

    chessboard[0][0] = 1
    print(chessboard)
    plt.imshow(chessboard, cmap="binary")
    plt.show()


grid()
