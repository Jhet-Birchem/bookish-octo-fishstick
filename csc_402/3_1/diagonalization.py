import numpy as np

def S_L_St(A):
  try:
    l, S = np.linalg.eig(A)
    Lambda = np.diag(l)
    return S, Lambda, np.transpose(S)
  except np.linalg.LinAlgError:
    print('We cannot diagonalize this matrix!')

def inverse_SLSt(A):
  try:
    l, S = np.linalg.eig(A)
    l_inv = [1/l[i] for i in range(len(l))]
    Lambda_inv = np.diag(l_inv)
    return np.matmul(np.matmul(S,Lambda_inv),np.transpose(S))
  except np.linalg.LinAlgError:
    print('We cannot diagonalize this matrix!')
    
A = np.array([[1,3],[3,-7]])
print('A =\n',A)
S, L, St = S_L_St(A)
A_inv = inverse_SLSt(A)
print('S =\n',S)
print('L =\n',L)
print('St =\n', St)
print('A^(-1) =\n',A_inv)
print('Built in Inverse: \n',np.linalg.inv(A))

