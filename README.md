# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step1 : 
### Step 2: 
### Step 3: Using the np.linalg.eig(),  we get two results (first is eigenvalue and second is eigenvector) of the given matrix.
### Step 4: 

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
