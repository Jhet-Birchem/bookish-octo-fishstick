import numpy as np

# A vector is an 1-dimensional array of numbers.
# E.g., input hardness vector of our cat brain model
v = np.array([0.11, 0.01, 0.98, 0.12, 0.98, 0.85, 0.03,
              0.55, 0.49, 0.99, 0.02, 0.31, 0.55, 0.87,
              0.63])
print('Vector v =',v)
print('List v =',list(v))

# Individual elements of the vector can be accessed through the square bracket operator with indices of the desired element  within thosesquare brackets.
# Index starts from zero, not one.
first_element = v[0]
third_element = v[2]
print(f'First Element = {first_element} Third Element = {third_element}')


# Negative indices are to be counted from the end of array.
# E.g., -1 refers to the last array element.
#       -2 refers to the second from last element.
last_element = v[-1]
second_last_element = v[-2]
print(f'Last Element = {last_element} Second to Last Element = {second_last_element}')

# A range of elements can be sliced off a vector using the colon operator
second_to_fifth_elements = v[1:4]
print(f'Second to Fifth Elements: {second_to_fifth_elements}')

# If nothing is specified on the left of the arrow, it implies beginning of array.
# If nothing is specified after the  colon it implies end of array.
first_to_third_elements = v[:2]
last_two_elements = v[-2:]
print(f'First to Third: {first_to_third_elements}  Last Two Elements: {last_two_elements}')

# Size of the vector
num_elements_in_v = len(v)
print(f'Number of Elements in v: {num_elements_in_v}')

# A matrix can be viewed as a 2-dimensional array of numbers. It can be thought of as a collection of row vectors, or a collection of column vectors.

# For example, the training set for the cat-brain problem can be expressed as a matrix.
# Each input instance to the machine can be viewed as a vector represented by a row in this matrix.
# Our training set consists of 15 examples, where each example is a row vector of size 2. So there are 15 rows and 2 columns.

X = np.array([[0.11, 0.09], [0.01, 0.02], [0.98, 0.91], [0.12, 0.21],
              [0.98, 0.99], [0.85, 0.87], [0.03, 0.14], [0.55, 0.45],
              [0.49, 0.51], [0.99, 0.01], [0.02, 0.89], [0.31, 0.47],
              [0.55, 0.29], [0.87, 0.76], [0.63, 0.24]])
print(f'X = \n{X}')

# Shape of the matrix is depicted as a list.
# The first list element represents the number of rows,
# the second list element represents the number of columns.
# Our training set consists of 15 examples, where each example is a row vector of size 2. So the shape is [15, 2].
print(f'Shape of the matrix is: {X.shape}')



# Slicing the matrix
# The matrix can be sliced using the indices representing the axes.

# Accessing individual elements of the matrix
# Each element is indexed by its row and column.
# Row, column indices start from 0

# Accessing first element of the matrix
first_element = X[0, 0]
print(f'First element X: {first_element}')

# Accessing 5th row, first column of the matrix
print(f'X[5][1]: {X[5][1]}')

# Accessing the rows
# Note the each row corresponds to one training example in our case.
# The : is shorthand to access all the elements of the selected rows
# i.e X[0, :] is equivalent of X[0, 0:num_columns]
row_1 = X[0, :] # First row has an index of 0
row_2 = X[1, 0:2] # Second row has an index of 1
print(f'Row 1: {row_1} Shape: {row_1.shape}')
print(f'Row 2: {row_2} Shape: {row_2.shape}')

# Accessing the columns
# The columns can similarly be accessed using the second axis.
# Note that each column corresponds to one feature i.e hardness or
# sharpness in our case.
column_1 = X[:, 0] # First column has an index of 0
column_2 = X[:, 1] #Second column has an index of 1
print(f'Column 1: {column_1} Shape: {column_1.shape}')
print(f'Column 2: {column_2} Shape: {column_2.shape}')

# Extracting sub-matrices. Slicing and dicing
# We can use a combination of row and column to
# slice and dice the matrix (i.e., extract sub-matrices).

# For example to access the first 3 training examples
first_3_training_examples = X[:3, ]
# X[:3, ] == X[0:3,] == X[:3, :] == X[:3, 0:num_columns]
# These are multiple ways to access the same elements.
print(f'First 3 training examples:\n{first_3_training_examples}')

# Selecting the hardness feature for  5th to 7th training examples
# Note that hardness corresponds to column 1
print(f'Hardness of 5-7 training examples is: {X[5:8, 1]} ')
