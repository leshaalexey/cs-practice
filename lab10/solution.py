import numpy as np

def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    m = np.array(matrix)

    return matrix[row_start:row_stop+1, column_start:column_stop+1].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    m = np.array(matrix)
    m[row_start:row_stop+1, column_start:column_stop+1] = value
    return m.tolist()

def matrix_vector_product(matrix, vector):
    m = np.array(matrix)
    v = np.array(vector)
    return (m @ vector).tolist()

def matrix_multiply(left, right):
    l = np.array(left)
    r = np.array(right)
    return (l @ r).tolist()

def transpose_matrix(matrix):
    m = np.array(matrix)
    return m.T.tolist()

def solve_system(matrix, vector):
    m = np.array(matrix)
    v = m = np.array(vector)
    return np.linalg.solve(m, v).tolist()

def tensor_channel_mean(tensor):
    t = np.array(tensor)
    return np.mean(t, axis=-1).tolist()

def point_distance(first, second):
    f = np.array(first)
    s = np.array(second)
    return round(np.linalg.norm(f-s), 6)
