import numpy as np

#############################################################

v = np.array([4,3])
w = np.array([5,1])
print('v =',v)
print('w =',w)

#############################################################

A = np.array([[4,5],[3,1]])
A_inv_real = np.array([[1/-11,-5/-11],[-3/-11,4/-11]])
print(A)
print(A_inv_real)
A_inv = np.linalg.inv(A)
print(A_inv)

#############################################################

np.matmul(A,A_inv_real)

#############################################################

v = np.array([4,3])
w = np.array([5,1])
print('v =',v)
print('w =',w)

print('')
print('Addition and Scalar Multiplication:')
print('v + w =',v + w)
print('-v =',-1*v)
print('2v =',2*v)
print('-1*v + 2*w =',-1*v + 2*w)
print('via Matrix/Vector Multiplication (row vector)')
A = np.array([[4,3],[5,1]])
print('-1*v + 2*w =',np.matmul([-1,2],A))
print('via Matrix/Vector Multiplication (column vector)')
A = np.array([[4,5],[3,1]])
print('-1*v + 2*w =',np.matmul(A,[-1,2]))

#############################################################

print('General Weights')
a = 13 #Change to any value
b = 37 #Change to any value
print(f'{a}*v + {b}*w = {a*v + b*w}')
print('via Matrix/Vector Multiplication (row vector)')
A = np.array([[4,3],[5,1]])
print(f'{a}*v + {b}*w = {np.matmul([a,b],A)}')
print('via Matrix/Vector Multiplication (column vector)')
A = np.array([[4,5],[3,1]])
print(f'{a}*v + {b}*w = {np.matmul(A,[a,b])}')

#############################################################

print('Finding Weights:')
print('via row vector')
y = np.array([3,5])
A = np.array([[4,3],[5,1]])
weights = np.matmul(y,np.linalg.inv(A))
print('[a,b] =',weights)

print('via column vector')
y = np.array([3,5])
A = np.array([[4,5],[3,1]])
weights = np.matmul(np.linalg.inv(A),y)
print('[a,b] =',weights)

#############################################################

print('Matrix/Vector Multiplication:')
A = np.array([[1,3],[3,7]])
print('A =\n',A)
B = np.array([[4,2],[3,1]])
print('B =\n',B)
print('A*B =\n',np.matmul(A,B))
print('B*A =\n',np.matmul(B,A))

#############################################################

print('Dot Product:')
print('v.w =',np.dot(v,w))
print('w.v =',np.dot(w,v))
print('Note: v.w = v^Tw')
print('v^Tw =',np.matmul(np.transpose(v),w))

#############################################################

print('Matrix Inverse:')
#It is often convient to define an inverse function!
def inverse(A):
  if np.linalg.det(A) == 0.0:
    return False
  return np.linalg.inv(A)

A = np.array([[1,2],[3,4]])
B = np.array([[1,3],[3,7]])
print('A =\n',A)
print('A^(-1) =\n', inverse(A))

print('B =\n',B)
print('B^(-1) =\n', inverse(B))

C = np.array([[4,2],[8,4]])
print('C =\n',C)
print('C^(-1) =\n', inverse(C))
