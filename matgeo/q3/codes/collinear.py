import numpy as np
import matplotlib.pyplot as plt
import ctypes

collinearity_lib = ctypes.CDLL('./collinear.so')
collinearity_lib.determinant.argtypes = [ctypes.POINTER(ctypes.c_double * 6)]
collinearity_lib.determinant.restype = ctypes.c_double

data = np.loadtxt('points.txt')
if data.shape[1] != 6:
    raise ValueError("Each line in points.txt must contain 6 values for 3 points.")


num_points = data.shape[0]  
if num_points == 0:
    raise ValueError("No points found in points.txt.")

points = data.reshape(num_points, 3, 2)

def solve_matrix(points):
    A = points[:, 0, :]
    B = points[:, 1, :]
    C = points[:, 2, :]

    matrix = np.array([[A[:, 0], A[:, 1], np.ones(num_points)],
                       [B[:, 0], B[:, 1], np.ones(num_points)],
                       [C[:, 0], C[:, 1], np.ones(num_points)]]).transpose(2, 0, 1)

    det_values = np.linalg.det(matrix)
    return det_values

def verify_collinearity(points):
    num_sets = points.shape[0]
    point_array_type = ctypes.c_double * 6  

    point_arrays = [point_array_type(*points[i].flatten()) for i in range(num_sets)]

    areas = np.array([collinearity_lib.determinant(ctypes.byref(point_array)) for point_array in point_arrays])

    return areas

det_values = solve_matrix(points)

c_det_values = verify_collinearity(points)

collinear_mask = np.isclose(det_values, 0) & np.isclose(c_det_values, 0)

collinear_points = points[collinear_mask]

if collinear_points.size > 0:
    plt.plot(collinear_points[:, 0, 0], collinear_points[:, 0, 1], 'o', label='Collinear Points A', color='red')
    plt.plot(collinear_points[:, 1, 0], collinear_points[:, 1, 1], 'o', label='Collinear Points B', color='green')
    plt.plot(collinear_points[:, 2, 0], collinear_points[:, 2, 1], 'o', label='Collinear Points C', color='blue')
    
    plt.plot(collinear_points[:, :, 0].T, collinear_points[:, :, 1].T, color='black')

plt.title('Collinear Lines for Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
plt.savefig("Figure_1.png")
