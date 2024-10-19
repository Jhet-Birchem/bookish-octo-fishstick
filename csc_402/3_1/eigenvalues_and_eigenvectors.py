import numpy as np

A = np.array([[3,-2],[-2,6]])
print('A =\n',A)
v = np.array([7,2])
print('v =',v)
print('Av =',np.matmul(A,v))
print('2v =',2*v)

np.linalg.eig(A)

print('===============================================')
l,S = np.linalg.eig(A)
print('First Eigenvalue/Eigenvector Pair:')
print('l_0 =',l[0],'with v_0 =',S[:,0])
print('Second Eigenvalue/Eigenvector Pair:')
print('l_1 =',l[1],'with v_1 =',S[:,1])
print('What does np.linalg.eig(A) return?')
print('l =',l)
print('S =\n',S)
print('===============================================')

#CLAIM: A = S*L*S^T

A = np.array([[3,-2],[-2,6]])
#A = np.array([[1,2,3],[2,4,5],[3,5,6]])
print('A =\n',A)
At = np.transpose(A)
print('A = A^T?\n',A == At)
l,S = np.linalg.eig(A)
Lambda = np.diag(l)

print('L =\n',Lambda)
print('S =\n',S)
print('St =\n',np.transpose(S))
print('S^(-1) =\n',np.linalg.inv(S))

print('SLS^T =\n',np.matmul(np.matmul(S,Lambda),np.transpose(S)))

#print('=======================================')
#import time.time()
#A = 100*np.random.rand(10,10)
#t = time.time()
#A_inv = np.linalg.inv(A)
#print('Inverse Found in', time.time() - t, 'Seconds')

#t = time.time()
#l,S = np.linalg.eig(A)
#print('Spectral Decomposition in', time.time() - t, 'Seconds')