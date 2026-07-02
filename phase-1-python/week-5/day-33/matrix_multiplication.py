import numpy as np

car_coordinates = np.array([2,3])
rotation_matrix = np.array([[1,0], [0,1]]) # 0 degree rotation
new_coordinates = rotation_matrix @ car_coordinates
print("Original coordinates:", car_coordinates)
print("New coordinates after rotation:", new_coordinates)


#variation 2
import numpy as np

car_coordinates = np.array([2,3])
rotation_matrix = np.array([[[1, 2], [3, 4], [5, 6]]]) # 0 degree rotation
new_coordinates = rotation_matrix @ car_coordinates
print("Original coordinates:", car_coordinates)
print("New coordinates after rotation:", new_coordinates)
