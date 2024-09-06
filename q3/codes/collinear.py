from ctypes import *
import numpy as np
import matplotlib.pyplot as plt

collinear = CDLL('./collinear.so')

collinear.is_collinear.restype = c_int
collinear.is_collinear.argtypes = [c_float, c_float, c_float, c_float, c_float, c_float]

def plot_collinear_points(k, x_1, y_1, x_2, y_2, x_3, y_3):
    plt.figure(figsize=(8, 6)) # Set the figure size for better visibility

    plt.scatter([x_1, x_2, x_3], [y_1, y_2, y_3], color='green')

    plt.text(x_1, y_1, f'({x_1:.1f}, {y_1:.1f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    plt.text(x_2, y_2, f'({x_2:.1f}, {y_2:.1f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    plt.text(x_3, y_3, f'({x_3:.1f}, {y_3:.1f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')

    plt.plot([x_1, x_2, x_3, x_1], [y_1, y_2, y_3, y_1], 'g--')

    plt.title(f'Collinear Points for k = {k:.1f}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.xlim(min(x_1, x_2, x_3) - 1, max(x_1, x_2, x_3) + 1)
    plt.ylim(min(y_1, y_2, y_3) - 1, max(y_1, y_2, y_3) + 1)

    plt.grid(True)
    plt.show()

def find_collinear_k():
    k_values = np.arange(-100.0, 100.1, 0.1) # Use numpy to include fractional values

    for k_float in k_values:
        x_1, y_1 = k_float + 1, 2 * k_float
        x_2, y_2 = 3 * k_float, 2 * k_float + 3
        x_3, y_3 = 5 * k_float - 1, 5 * k_float

        if collinear.is_collinear(c_float(x_1), c_float(y_1), c_float(x_2), c_float(y_2), c_float(x_3), c_float(y_3)):
            rounded_k = round(k_float, 1)
            print(f"Points are collinear when k = {rounded_k}")
            plot_collinear_points(rounded_k, x_1, y_1, x_2, y_2, x_3, y_3)

find_collinear_k()
plt.savefig("q3_1.png")
plt.savefig("q3_2.png")
