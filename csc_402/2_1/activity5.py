import numpy as np

############################
#Problem 1 - Multiplication
############################
print('############################')
print('# Problem 1 - Multiplication')
print('############################')
A = np.array([[8,6],[7,5]])
B = np.array([[3,0],[9,9]])
C = np.matmul(A,B)
print('C =\n',C)

A = [[8,6],[7,5]] #Here A is just a list
B = [[3,0],[9,9]] #Here B is just a list
def mat_mul(A,B):
    """
    This function computes C = A*B
    """
    m = len(A) #Number of rows in X
    q = len(A[0]) #Number of columns in X
    n = len(B[0]) #Number of columns in Y

    if q != len(B):
        return False #Ensure the # columns of A = # rows of B
    result = []
    for i in range(m):
        result.append([])
        for j in range(n):
            result[i].append(0)
            for k in range(q):
                result[i][j] += A[i][k] * B[k][j]
    return result

print('C = ',mat_mul(A,B)) #Note the result of matrix_multiply(A,B) is a list

#Or we have a more pythony way of doing multiplicaiton
def mat_mul_v2(A,B):
  """
  This function computes C = A*B (no check on columns = rows)
  """
  return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print('C = ',mat_mul_v2(A,B)) #Note the result of matrix_multiply(A,B) is a list

A = np.array([[8,6,7,5],[3,0,9,9],[1,3,3,7]])
B = np.array([[1,7],[3,3],[3,3],[7,1]])

############################
#Problem 2 - Determinats
############################
print('############################')
print('# Problem 2 - Determinants')
print('############################')
A = np.array([[8,6,7],[5,3,0],[9,4,2]])
print('A =\n',A)
print('det(A) = |A| =',np.linalg.det(A))

############################
#Problem 3 - Inverses
############################
print('############################')
print('#Problem 3 - Inverses')
print('############################')
A = np.array([[8,6],[7,5]])
B = np.array([[3,0],[9,9]])
print('A =\n',A)
print('A^(-1) =\n',np.linalg.inv(A))

A = np.array([[8,6,7],[5,3,0],[9,4,2]])
print('A =\n',A)
print('A^(-1) =\n',np.linalg.inv(A))