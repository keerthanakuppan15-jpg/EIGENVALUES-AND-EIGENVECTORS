#Program to find the eigen values and eigen vectors.
#Developed by:keerthana k
#RegisterNumber:212225230137
import numpy as np
matrix= np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])
eig_values,eig_vectors=np.linalg.eig(matrix)
print("Eigen values are {} and Eigen Vectors are {}".format(eig_values,eig_vectors))
