import numpy as np

#f(x,y) = x^3 + y^3 - 3xy + 4
def f(point):
  return point[0]**3 + point[1]**3 - 3*point[0]*point[1] + 4

def fx(point):
  return 3*point[0]**2 - 3*point[1]

def fy(point):
  return 3*point[1]**2 - 3*point[0]

def gradf(point):
  return np.array([fx(point),fy(point)])

###############################################
#
#Standard Gradient Descent (GD)
#
###############################################
def grad_descent(initial,learning_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    #print(n,current_point,update_vector)
    update_vector =learning_rate*gradf(current_point)
    current_point = current_point - update_vector
  return current_point

starting_points = [[i,j] for i in range(1,5) for j in range(-2,3)]

initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 200

print('=================================================================')
print('Gradient Descent on f(x,y) = 3x - x^3 - 2y^2 + y^4')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Multiple Starting Points!')
for p in starting_points:
  print(p,' \t|',grad_descent(p,learning_rate,num_trials))
print('=================================================================')

###############################################
#
#Gradient Descent (GD) with Momentum
#
###############################################
def grad_descent_with_momentum(initial,learning_rate,momentum_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    #print(n,current_point)
    update_vector = learning_rate*gradf(current_point) + momentum_rate*update_vector
    current_point = current_point - update_vector
  return current_point

starting_points = [[i,j] for i in range(1,5) for j in range(-2,3)]

initial_guess = np.array([4,2])
learning_rate = 0.01
momentum_rate = 0.5
num_trials = 200

print('Gradient Descent (with momentum) on f(x,y) = 3x - x^3 - 2y^2 + y^4')
print('Initial Guess:',initial_guess)
print('Learning Rate:',learning_rate)
print('Momentum Rate:',momentum_rate)
print('Number of Iterations:', num_trials)
print(grad_descent_with_momentum(initial_guess,learning_rate,momentum_rate,num_trials))
print('Multiple Starting Points!')
for p in starting_points:
  print(p,' \t|',grad_descent_with_momentum(p,learning_rate,momentum_rate,num_trials))
print('=================================================================')

###############################################
#
#Accelerated Gradient Descent
#
###############################################
def accel_grad_descent(initial,learning_rate,momentum_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    #print(n,current_point)
    lookahead_point = current_point - momentum_rate * update_vector
    update_vector = learning_rate*gradf(lookahead_point) + momentum_rate*update_vector
    current_point = current_point - update_vector
  return current_point

starting_points = [[i,j] for i in range(1,5) for j in range(-2,3)]

initial_guess = np.array([4,2])
learning_rate = 0.01
momentum_rate = 0.5
num_trials = 200

print('Accelerated Gradient Descent on f(x,y) = 3x - x^3 - 2y^2 + y^4')
print('Initial Guess:',initial_guess)
print('Learning Rate:',learning_rate)
print('Momentum Rate:',momentum_rate)
print('Number of Iterations:', num_trials)
print(accel_grad_descent(initial_guess,learning_rate,momentum_rate,num_trials))
print('Multiple Starting Points!')
for p in starting_points:
  print(p,' \t|',accel_grad_descent(p,learning_rate,momentum_rate,num_trials))
print('=================================================================')

###############################################
#
#Gradient Descent - updated learning rate
#
###############################################
def grad_descent_updated_learning_rate(initial,learning_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    #print(n,current_point,update_vector)
    learning_rate = learning_rate / (1 / (n+1)*(n+1))
    update_vector = learning_rate*gradf(current_point)
    current_point = current_point - update_vector
  return current_point

starting_points = [[i,j] for i in range(1,5) for j in range(-2,3)]

initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 200

print('=================================================================')
print('Gradient Descent - updated learning rate on f(x,y) = 3x - x^3 - 2y^2 + y^4')
print('Initial Guess:',initial_guess)
print('m_n: 1/(n+1)')
print('Initial Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print(grad_descent_updated_learning_rate(initial_guess,learning_rate,num_trials))
print('Multiple Starting Points!')
for p in starting_points:
  print(p,' \t|',grad_descent_updated_learning_rate(p,learning_rate,num_trials))
print('=================================================================')

###############################################
#
#Addtional Function
#
###############################################
#f(x,y) = 3x - x^3 - 2y^2 + y^4
#def f(point):
#  return 3*point[0] - point[0]**3 - 2*point[1]**2 + point[1]**4

#def fx(point):
#  return 3 - 3*point[0]**2

#def fy(point):
#  return -4*point[1] + 4*point[1]**3

#def gradf(point):
#  return np.array([fx(point),fy(point)])

