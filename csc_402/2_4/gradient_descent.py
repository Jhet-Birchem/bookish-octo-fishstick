import numpy as np

#########################################################################

def f(point):
  return point[0]**4 + point[1]**4 - 4*point[0]*point[1] + 1

def fx(point):
  return 4*point[0]**3 - 4*point[1]

def fy(point):
  return 4*point[1]**3 - 4*point[0]

def gradf(point):
  return np.array([fx(point),fy(point)])

#########################################################################

def grad_descent(initial,learning_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    print(n,current_point,update_vector)
    update_vector = learning_rate*gradf(current_point)
    current_point = current_point - update_vector
  return current_point

initial_guess = np.array([4,-4])
learning_rate = 0.01
num_trials = 200
print('=================================================================')
print('Gradient Descent on f(x,y) = x^4 + y^4 - 4xy + 1')
print('Initial Guess:',initial_guess)
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print(grad_descent(initial_guess,learning_rate,num_trials))
print('=================================================================')

#########################################################################

def grad_descent_error(initial,learning_rate,error_bound):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  n = 0
  while n < 1000:
    #We will break out if we find ||current - previous||^2 < error_bound.
    #However, we may fall off a cliff and never stabalize!

    #print(n,current_point,update_vector)
    update_vector = learning_rate*gradf(current_point)
    current_point = current_point - update_vector
    if np.dot(update_vector,update_vector) < error_bound:
      return current_point
    n += 1
    
initial_guess = np.array([4,2])
learning_rate = 0.01
error_test = 0.000001
print('Gradient Descent on f(x,y) = x^4 + y^4 - 4xy + 1')
print('Initial Guess:',initial_guess)
print('Learning Rate:',learning_rate)
print('Error Bound:', error_test)
print(grad_descent_error(initial_guess,learning_rate,error_test))
print('=================================================================')

#########################################################################

def grad_descent_with_momentum(initial,learning_rate,momentum_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    #print(n,current_point)
    update_vector = learning_rate*gradf(current_point) + momentum_rate*update_vector
    current_point = current_point - update_vector
  return current_point

initial_guess = np.array([4,-2])
learning_rate = 0.01
momentum_rate = 0.01
num_trials = 50
print('Gradient Descent (with momentum) on f(x,y) = x^4 + y^4 - 4xy + 1')
print('Initial Guess:',initial_guess)
print('Learning Rate:',learning_rate)
print('Momentum Rate:',momentum_rate)
print('Number of Iterations:', num_trials)
print(grad_descent_with_momentum(initial_guess,learning_rate,momentum_rate,num_trials))
print('=================================================================')

#########################################################################