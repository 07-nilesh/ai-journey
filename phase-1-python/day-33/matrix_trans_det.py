import numpy as np

house_features = np.array([2,1]) # 2 bedrooms, 1 bathroom

space_stretcher = np.array([[3,1],[0,2]]) # Stretching matrix

transformed_features = space_stretcher @ house_features
print("Original features:", house_features)
print("Transformed features:", transformed_features)
determinant = np.linalg.det(space_stretcher)
print("Determinant of the transformation matrix:", determinant)

#variation 1
import numpy as np

house_features = np.array([2,1]) 

space_stretcher = np.array([[-1,0],[0,1]]) # Stretching matrix

transformed_features = space_stretcher @ house_features
print("Original features:", house_features)
print("Transformed features:", transformed_features)
determinant = np.linalg.det(space_stretcher)
print("Determinant of the transformation matrix:", determinant)

#variation 2
import numpy as np

house_features = np.array([2,1]) 
collapse_matrix = np.array([[1,2],[2,4]]) # Collapsing matrix
space_stretcher = np.array([[-1,0],[0,1]]) # Stretching matrix

transformed_features = space_stretcher @ house_features
collapsed_features = collapse_matrix @ transformed_features
print("Original features:", house_features)
print("Transformed features:", transformed_features)
print("Collapsed features:", collapsed_features)
determinant = np.linalg.det(space_stretcher)
determinant_collapse = np.linalg.det(collapse_matrix)

print("Determinant of the transformation matrix:", determinant)
print("Determinant of the collapse matrix:", determinant_collapse)