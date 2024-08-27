from ctypes import*
section=CDLL('./section.so')
class Point(Structure):
    _fields_=[("x",c_float),
            ("y",c_float)]
section=section.section
section.restype = Point
x1, y1 = -6, 10 
x2, y2 = 3, -8
m, n = 2, 7
result = section(c_float(x1), c_float(y1), c_float(x2), c_float(y2), c_float(m), c_float(n))
print(f"section point:({result.x},{result.y})")
import matplotlib.pyplot as plt
plt.scatter([x1, x2], [y1, y2],
        color='blue', label='orginal Points')
plt.scatter([result.x], [result.y],
        color='red', label='section Point')
plt.plot([x1, x2], [y1, y2], 'g--')
plt.text(x1, y1, f'({x1}, {y1})', 
fontsize=12,
verticalalignment='bottom', 
horizontalalignment='right')
plt.text(x2, y2, f'({x2}, {y2})', 
fontsize=12, 
verticalalignment='bottom', 
horizontalalignment='left')
plt.text(result.x, result.y, f'({result.x}, {result.y})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Section Formula')
plt.savefig("q2.png")


