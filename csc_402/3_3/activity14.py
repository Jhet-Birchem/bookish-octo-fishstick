import numpy as np
import matplotlib.pyplot as plt

x_0 = np.array([8,7,3,9])
x_1 = np.array([6,5,0,9])

# Create the data matrix with x0, x1 as columns
X = np.column_stack((x_0, x_1))
print('X =\n',X)

mean_vec = np.array([np.mean(X,axis=0)]).reshape((-1, 1))
print('Mean Vector: \n{}\n'.format(mean_vec))

#We set rowvar as False as each column is a variable
covariance_matrix = np.cov(X, rowvar=False)

print('C =\n',covariance_matrix)

principal_values, principal_components = np.linalg.eig(covariance_matrix)

print('Principal Values:\n{}\n'.format(principal_values))
print('Principal Components:\n{}\n'.format(principal_components))

# Find the index with highest principal value
major_index = np.argmax(principal_values)
minor_index = np.argmin(principal_values)

first_princpal_vec = principal_components[:,major_index]
first_princpal_vec = first_princpal_vec.reshape((-1, 1))
print('First (Major) Principal Vector:\n{}\n'.format(first_princpal_vec))

second_princpal_vec = principal_components[:,minor_index]
second_princpal_vec = second_princpal_vec.reshape((-1, 1))
print('Minor Principal Vector:\n{}\n'.format(second_princpal_vec))

print('==============================')
print('Part f')
print('==============================')
#u = np.array([1,0])
#u = np.array([1/np.sqrt(2),1/np.sqrt(2)])
u = first_princpal_vec
print('u =',u)
X_proj = np.dot(X, u)
print('X_proj =',X_proj)
print('Var(X_proj) = ',np.var(X_proj,ddof=1))
print('u^TCu = ', np.matmul(np.matmul(np.transpose(u),covariance_matrix),u))

plt.figure()
plt.scatter(X[:, 0], X[: , 1], color="green")
plt.xlabel('X0')
plt.ylabel('X1')

line = np.array([first_princpal_vec * t + mean_vec for t in np.linspace(-7, 7, 100)])
plt.plot(line[:, 0], line[:, 1],color="blue")

#plt.scatter(X_proj[:, 0], np.zeros_like(X_proj[:, 0]))

plt.show()
