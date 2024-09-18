import numpy as np

def pseudo_inverse(A):
    return np.matmul(np.linalg.inv(np.matmul(np.transpose(A), A)), np.transpose(A))

v = np.array([4,3])
vs = np.array([-3,4])
w = np.array([5,1])

print('||v|| =',np.linalg.norm(v))
print('||v*|| =',np.linalg.norm(vs))
print('||w|| =',np.linalg.norm(w))
print('')
print('||v||^2 = v.v =',np.dot(v,v))
print('||v*||^2 = v.v =',np.dot(v,v))
print('||w||^2 = w.w =',np.dot(w,w))
print('')
print('v - v* =',v - vs)
print('||v - v*||^2 = ',np.dot(v-vs,v-vs))
print('')
print('v - w =',v - w)
print('||v - w||^2 =',np.dot(v-w,v-w))

print('====================================')
print('# Illness Example')
print('====================================')
X = np.array([
  [0,0,0,0,0],
  [0,0,0,0,1],
  [1,1,1,0,0],
  [1,0,0,1,0],
  [1,1,0,0,0],
  [1,0,1,0,0]])
#print('X =\n',X)

A = np.column_stack((X, np.ones(6)))
#print('A =\n',A)

y = np.array([-1,1,1,-1,1,1])
#print('y =\n',y)

wb = np.array([1,1,1,1,1,-1])
#wb = np.array([2,0,0,-2,2,-1])

print('For w_b =',wb,'we obtain:')
norm_squared = np.dot(np.matmul(A,wb) - y,np.matmul(A,wb) - y)
print('||Aw_b - y||^2 =',norm_squared)

wb = np.matmul(pseudo_inverse(A),y)
print('For w_b =',wb,'we obtain:')
norm_squared = np.dot(np.matmul(A,wb) - y,np.matmul(A,wb) - y)
print('||Aw_b - y||^2 =',norm_squared)

print('====================================')
print('# AND Example')
print('====================================')
X = np.array([
  [0,0],
  [0,1],
  [1,0],
  [1,1]])
#print('X =\n',X)

y = np.array([-1,-1,-1,1])
#print('y =\n',y)

A = np.column_stack((X, np.ones(len(X))))


wb = np.array([1,1,-1])

print('For w_b =',wb,'we obtain:')
norm_squared = np.dot(np.matmul(A,wb) - y,np.matmul(A,wb) - y)
print('||Aw_b - y||^2 =',norm_squared)

wb = np.matmul(pseudo_inverse(A),y)
print('For w_b =',wb,'we obtain:')
norm_squared = np.dot(np.matmul(A,wb) - y,np.matmul(A,wb) - y)
print('||Aw_b - y||^2 =',norm_squared)

