# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
Step 1:

Start the program and import the NumPy library using import numpy as np to perform matrix operations.

Step 2:

Define the given square matrix using a NumPy array.

Step 3:

Use the built-in function np.linalg.eig() to compute the eigenvalues and eigenvectors of the given matrix.

Step 4:

Display the eigenvalues and eigenvectors as the output.

## Program:
```#Program to find the eigen values and eigen vectors.
#Developed by:keerthana k
#RegisterNumber:212225230137
import numpy as np
matrix= np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])
eig_values,eig_vectors=np.linalg.eig(matrix)
print("Eigen values are {} and Eigen Vectors are {}".format(eig_values,eig_vectors))
```

## Output:<img width="1920" height="1080" alt="Screenshot 2026-02-10 113658" src="https://github.com/user-attachments/assets/cf550b40-1d8b-4433-a109-42f488b62855" />

## Result:
Thus the Eigenvalue and Eigenvector is successfully solved using python program
