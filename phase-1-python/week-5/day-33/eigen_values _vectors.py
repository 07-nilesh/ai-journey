import numpy as np

dataset_matrix= np.array([[3,1],[0,2]])
eigenvalues, eigenvectors = np.linalg.eig(dataset_matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
row=eigenvectors[:,0]
mul=dataset_matrix @ row
print("Matrix multiplied by the first eigenvector:", mul)
mul2=eigenvalues[0]*row
print("First eigenvalue multiplied by the first eigenvector:", mul2)

#variation 1
import numpy as np

dataset_matrix= np.array([[3,0],[0,2]])
eigenvalues, eigenvectors = np.linalg.eig(dataset_matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)