#Strassen's Algorithm using Recursion
import numpy as np

x = np.array([[1, 2], [2, 3]])
y = np.array([[2, 3], [3, 4]])


def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, col2], matrix[:row2, :col2], matrix[:row2, :col2]


def strassen_recur(x, y):
    #splitting the matrices into quadrants.
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    #computing the 7 products
    p1 = strassen_recur(a, f - h)
    p2 = strassen_recur(a + b, h)
    p3 = strassen_recur(c + d, e)
    p4 = strassen_recur(d, g - e)
    p5 = strassen_recur(a + d, e + h)
    p6 = strassen_recur(b - d, g + h)
    p7 = strassen_recur(a - c, e + f)

    #computing the values of the 4 quadrants of the final matrix c
    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)

    #combining the 4 quadrants into a single matrix by stacking horizontally and vertically
    c = np.vstack((np.hstack((c1, c2)), np.hstack((c3, c4))))

    return c


print(strassen_recur(x, y))