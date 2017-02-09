"""utility.py
"""

def matrix_mult(A, B):
    temp_b = zip(*B)
    return [[sum(ea * eb for ea, eb in zip(a, b)) for b in temp_b] for a in A]
