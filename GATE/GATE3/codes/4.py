import matplotlib.pyplot as plt
import numpy as np

# Define time intervals
T = 1

# Define each segment of the plot
t1 = np.array([0, T])       # Constant from 0 to T
y1 = np.array([1, 1])

t2 = np.array([T, T])       # Drop from 1 to 0 at T
y2 = np.array([1, 0])

t3 = np.linspace(T, 2*T, 100)  # Smooth increase from 0 to 1 between T and 2T
y3 = np.linspace(0, 1, 100)

t4 = np.array([2*T, 3*T])   # Constant at 1 from 2T onwards
y4 = np.array([1, 1])

# Combine all time and value segments
t = np.concatenate(([0], t1, t2, t3, t4))
y = np.concatenate(([0], y1, y2, y3, y4))

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(t, y, color='black')
plt.ylim(-0.2, 1.2)

# Add x and y axes with arrows
plt.arrow(0, 0, 3.2*T, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')  # x-axis
plt.arrow(0, 0, 0, 1.3, head_width=0.05, head_length=0.05, fc='black', ec='black')   # y-axis

# Add labels and text
plt.xlabel('t')
plt.xticks([0, T, 2*T, 3*T], ['0', 'T', '2T', '3T'])
plt.yticks([0, 1])
plt.text(T, -0.1, 'T', ha='center')
plt.text(2*T, -0.1, '2T', ha='center')

plt.grid(False)
plt.show()

