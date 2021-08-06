import matplotlib.pyplot as plt
import numpy as np
import time


# def grid():

#     chessboard = np.zeros((6, 6))

#     chessboard[0][0] = 1
#     print(chessboard)
#     plt.grid()
#     plt.imshow(chessboard, cmap="binary")
#     plt.show()


# grid()
def f(i: int, f: float, s: str) -> None:
    print(str(i) + " " + str(f) + " " + str(s))


l = [45, 4.9, "XX"]
f(*l)  # -> print 45 4.9 XX
