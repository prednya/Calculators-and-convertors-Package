from sympy import *

def RankNullity(M):
    Mat_final = Matrix(M)
    # print("Matrix : {} ".format(Mat_final))
    n = Mat_final.shape[1]
    rank_value = Mat_final.rank()
    nullity_value = n - rank_value
    return (rank_value, nullity_value)

# print(RankNullity([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]]))