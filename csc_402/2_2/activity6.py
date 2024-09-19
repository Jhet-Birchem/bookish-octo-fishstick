import numpy as np

def pseudo_inverse(A):
    return np.matmul(np.linalg.inv(np.matmul(np.transpose(A), A)), np.transpose(A))

############################
# Problem 1
############################
print('############################')
print('# Problem 1')
print('############################')
#Key Function Reminders
#np.linalg.norm(v) #Gives ||v||
#np.dot(v,w) #Gives v.w
#np.dot(v,v) #Gives v.v = ||v||^2

v = np.array([1,3])
w = np.array([3,7])
print('v =',v)
print('w =',w)

print("\n a:")
print(np.linalg.norm(v))
print(np.dot(v,v))

print("\n b:")
print(np.linalg.norm(w))
print(np.dot(w,w))

print("\n c:")
print(np.dot(v,w))

print("\n d:")
print(np.linalg.norm(v-w))
print(np.dot(v-w,v-w))

print("\n e:")
if ((np.dot(v,w))**2 <= (np.linalg.norm(v)**2)*(np.linalg.norm(w)**2)):
    print("The Cauchy-Schwartz Inequality is SATISFIED.")
else:
    print("The Cauchy-Schwartz Inequality is NOT SATISFIED.")


############################
# Problem 2
############################
print('')
print('############################')
print('# Problem 2')
print('############################')

v = np.array([1,3,3,3,7])
w = np.array([1,-4,3,-4,2])
print('v =',v)
print('w =',w)

print("\n a:")
print(np.dot(v,v))

print("\n b:")
print(np.dot(w,w))

print("\n c:")
print(np.dot(v,w))

print("\n d:")
print(np.linalg.norm(v-w))
print(np.dot(v-w,v-w))

############################
# Problems 3 and 4
############################
print('')
print('############################')
print('# Problems 3 + 4')
print('############################')

# print('# AND Example')
# print('############################')
# #AND Example!
# X = np.array([
#   [0,0],
#   [0,1],
#   [1,0],
#   [1,1]])
# A = np.column_stack((X, np.ones(len(X))))
# y = np.array([-1,-1,-1,1])

# print('# OR Example')
# print('############################')
# #OR Example!
# X = np.array([
#   [0,0],
#   [0,1],
#   [1,0],
#   [1,1]])
# A = np.column_stack((X, np.ones(len(X))))
# y = np.array([-1,1,1,1])

print('# XOR Example')
print('############################')
#XOR Example!
X = np.array([
  [0,0],
  [0,1],
  [1,0],
  [1,1]])
A = np.column_stack((X, np.ones(len(X))))
y = np.array([-1,1,1,-1])

#Guess values for wb
wb = np.array([1,1,0])
print('For w_b =',wb,'we obtain:')
norm_squared = np.dot(np.matmul(A,wb) - y,np.matmul(A,wb) - y)
print('||Aw_b - y||^2 =',norm_squared)

#Using Pseudo-Inverse to find wb (i.e., Spoilers Ahead!)
wb = np.matmul(pseudo_inverse(A), y)
print('For w_b =',wb,'we obtain:')
norm_squared = np.dot(np.matmul(A,wb) - y,np.matmul(A,wb) - y)
print('||Aw_b - y||^2 =',norm_squared)

