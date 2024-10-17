import numpy as np

A = np.array([[3,-2],[-2,6]])
print('A =\n',A)

print('===============================================')
l,S = np.linalg.eig(A)
print('First Eigenvalue/Eigenvector Pair:')
print('l_0 =',l[0],'with v_0 =',S[:,0])
print('Second Eigenvalue/Eigenvector Pair:')
print('l_1 =',l[1],'with v_1 =',S[:,1])
print('===============================================')

Lambda = np.diag(l)
#Lambda = np.array([[2,0],[0,7]])
print('A =\n',A)
print('L =\n',Lambda)
print('S =\n',S)
St = np.transpose(S)
print('St =\n',St)

print('S*St =\n',np.matmul(S,St))
print('SLS^T =\n',np.matmul(np.matmul(S,Lambda),St))

A_inv = np.linalg.inv(A)
print('A^(-1) =\n',A_inv)
print('S(L^(-1))S^T =\n',np.matmul(np.matmul(S,np.linalg.inv(Lambda)),St))

A2 = np.linalg.matrix_power(A,2)
print('A**2 =\n',A2)
print('S(L^(2))S^T =\n',np.matmul(np.matmul(S,np.linalg.matrix_power(Lambda,2)),St))

A20 = np.linalg.matrix_power(A,20)
print('A**20 =\n',A20)
print('S(L^(20))S^T =\n',np.matmul(np.matmul(S,np.linalg.matrix_power(Lambda,20)),St))

#Lambda_inv = np.array([[1/2,0],[0,1/7]])
#Lambda_inv = np.diag([1/a for a in l])
#Lambda2 = np.array([[2**2,0],[0,7**2]])
#Lambda2 = np.diag([a**2 for a in l])
#Lambda10 = np.array([[2**10,0],[0,7**10]])
#Lambda10 = np.diag([int(a**10) for a in l])

