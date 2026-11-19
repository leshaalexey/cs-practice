import numpy as np

def make_hours():
    return np.arange(0, 22, 3)

def vector_report(values):
    a = np.array(values, dtype=float)

    return {
        "third": a[2],
        "last": a[-1],
        "middle": a[2:6],
        "every_second": a[::2],
        "reversed": a[::-1],
    }

def change_vector(values):
    a = np.asarray(values, dtype=float).copy()
    a[1:3] = 99
    a[::2] = -1
    return a

def cap_above(values, limit):
    a = np.asarray(values, dtype=float).copy()
    a[a > limit] = limit
    return a

def celsius_to_fahrenheit(values):
    a = np.array(values, dtype=float)
    return a * 9 / 5 + 32
