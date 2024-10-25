import numpy as np
import matplotlib.pyplot as plt

x_0 = np.array([1,3,2,4])
x_1 = np.array([3,7,4,10])

# Create the data matrix with x0, x1 as columns
X = np.column_stack((x_0, x_1))
print('X =\n',X)

mean_vec = np.array([np.mean(X,axis=0)]).reshape((-1, 1))
print('Mean Vector: \n',mean_vec)

#We set rowvar as False as each column is a variable
covariance_matrix = np.cov(X, rowvar=False)


print('C =\n',covariance_matrix)

principal_values, principal_components = np.linalg.eig(covariance_matrix)

print(f'Principal Values:\n{principal_values}\n')
print(f'Principal Components:\n{principal_components}\n')

# Find the index with highest principal value
major_index = np.argmax(principal_values)
minor_index = np.argmin(principal_values)

first_princpal_vec = principal_components[:,major_index]
first_princpal_vec = first_princpal_vec.reshape((-1, 1))
print(f'First (Major) Principal Vector:\n{first_princpal_vec}\n')

second_princpal_vec = principal_components[:,minor_index]
second_princpal_vec = second_princpal_vec.reshape((-1, 1))
print(f'Minor Principal Vector:\n{second_princpal_vec}\n')

plt.figure()
plt.scatter(X[:, 0], X[: , 1], color="green")
plt.xlabel('X0')
plt.ylabel('X1')

line = np.array([first_princpal_vec * t + mean_vec for t in np.linspace(-7, 7, 100)])
plt.plot(line[:, 0], line[:, 1],color="blue")

plt.show()
