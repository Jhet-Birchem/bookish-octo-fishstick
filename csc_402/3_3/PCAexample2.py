import numpy as np
import matplotlib.pyplot as plt

def pca(X):
    """
    X: Matrix such that rows correspond to data points and columns correspond to the features.
    Returns principal values, principal components
    """
    assert len(X.shape) == 2
    #We set rowvar as False as each column is a variable
    covariance_matrix = np.cov(X, rowvar=False)
    l, e = np.linalg.eig(covariance_matrix)
    return l, e

N = 100
# We create a random feature vector (Mean 0 SD 100)
x_0 = np.random.normal(0, 100, N)

# Then we create another vector which is highly correlated:
# x1 = 2 * x0.
# We add random noise (Mean 0 SD 50) to this second feature.
x_1 = 2 * x_0 + np.random.normal(0, 20, N)

# Create the data matrix with x0, x1 as columns
X = np.column_stack((x_0, x_1))
mean_vec = np.array([np.mean(X,axis=0)]).reshape((-1, 1))
print('Mean Vector: \n{}\n'.format(mean_vec))

principal_values, principal_components = pca(X)
print('Principal values: {}\n'.format(principal_values))

# Find the index with highest principal value
major_index = np.argmax(principal_values)
minor_index = np.argmin(principal_values)

first_princpal_vec = principal_components[:,major_index]
first_princpal_vec = first_princpal_vec.reshape((-1, 1))
print('First (Major) Principal Vector:\n{}\n'.format(first_princpal_vec))

second_princpal_vec = principal_components[:,minor_index]
second_princpal_vec = second_princpal_vec.reshape((-1, 1))
print('Minor Principal Vector:\n{}\n'.format(second_princpal_vec))

plt.figure()
plt.scatter(X[:, 0], X[: , 1], color="green")
plt.xlabel('X0')
plt.ylabel('X1')
# Plot the first principal component. It should
# be along the principal spread, showing us the
# major pattern (correlation) in the data.
line = np.array([first_princpal_vec * t + mean_vec for t in np.linspace(-300, 300, 100)])
plt.plot(line[:, 0], line[:, 1],color="blue")

line = np.array([second_princpal_vec * t + mean_vec for t in np.linspace(-50, 50, 100)])
plt.plot(line[:, 0], line[:, 1],color="red")

plt.show()
