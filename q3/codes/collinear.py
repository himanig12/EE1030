from ctypes import *
import numpy as np
import matplotlib.pyplot as plt

collinear = CDLL('./collinear.so')

collinear.is_collinear.restype = c_int
collinear.is_collinear.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float]

def plot_collinear_points(k, x1, y1, x2, y2, x3, y3):
    plt.figure(figsize=(8, 6)) # Set the figure size for better visibility

    plt.scatter([x1, x2, x3], [y1, y2, y3], color='green')

    plt.text(x1, y1, f'({x1:.1f}, {y1:.1f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    plt.text(x2, y2, f'({x2:.1f}, {y2:.1f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    plt.text(x3, y3, f'({x3:.1f}, {y3:.1f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')

    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'g--')

    plt.title(f'Collinear Points for k = {k:.1f}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.xlim(min(x1, x2, x3) - 1, max(x1, x2, x3) + 1)
    plt.ylim(min(y1, y2, y3) - 1, max(y1, y2, y3) + 1)

    plt.grid(True)
    plt.show()

def find_collinear_k():
    k_values = np.arange(-100.0, 100.1, 0.1) # Use numpy to include fractional values

    for k_float in k_values:
        x1, y1 = k_float + 1, 2 * k_float
        x2, y2 = 3 * k_float, 2 * k_float + 3
        x3, y3 = 5 * k_float - 1, 5 * k_float

        if collinear.is_collinear(c_float(x1), c_float(y1), c_float(x2), c_float(y2), c_float(x3), c_float(y3)):
            rounded_k = round(k_float, 1)
            print(f"Points are collinear when k = {rounded_k}")
            plot_collinear_points(rounded_k, x1, y1, x2, y2, x3, y3)

find_collinear_k()
plt.savefig("q3_1.png")
plt.savefig("q3_2.png")
