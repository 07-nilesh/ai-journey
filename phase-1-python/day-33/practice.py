import numpy as np
import matplotlib.pyplot as plt

linear_2d=np.array([2,3])
stretch_matrix=np.array([[1,0],[0,0]])
transformed_2d=stretch_matrix @ linear_2d
print("Original 2D point:", linear_2d)
print("Transformed 2D point:", transformed_2d)

fig,ax=plt.subplots(figsize=(6,6))
# To draw an arrow from (0,0) to (x,y):
# ax.quiver(origin_x, origin_y, target_x, target_y, angles='xy', scale_units='xy', scale=1)
i_hat=np.array([1,0])
j_hat=np.array([0,1])
transformed_i = stretch_matrix @ i_hat
transformed_j = stretch_matrix @ j_hat
ax.quiver(0, 0, 2, 3, angles='xy', scale_units='xy', scale=1, color='blue')
ax.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='green')
ax.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='green')
ax.quiver(0, 0, transformed_i[0], transformed_i[1], angles='xy', scale_units='xy', scale=1, color='red')
ax.quiver(0, 0, transformed_j[0], transformed_j[1], angles='xy', scale_units='xy', scale=1, color='red')
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_aspect('equal')
ax.set_title("Original vs Transformed Point")
plt.grid()
plt.tight_layout()
plt.show()  