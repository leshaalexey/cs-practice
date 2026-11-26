import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    a = np.array(values, dtype=float).tolist()

    return {
        "third": a[2],
        "last": a[-1],
        "middle": a[2:6],
        "every_second": a[::2],
        "reversed": a[::-1],
    }

def change_vector(values):
    a = np.asarray(values, dtype=float).copy()
    a[2:4] = 99
    a[::2] = -1
    return a.tolist()

def cap_above(values, limit):
    a = np.asarray(values, dtype=float).copy()
    a[a > limit] = limit
    return a.tolist()

def celsius_to_fahrenheit(values):
    a = np.array(values, dtype=float)
    return (a * 9 / 5 + 32).tolist()
