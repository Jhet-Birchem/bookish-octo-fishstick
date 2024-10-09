import numpy as np

#################################
# Problem 3
#################################
#f(x,y) = (x - 1)**2 + (y - 333)**2 + (x + y - 10)^2
#
#You will have to define f, fx, and fy below

#Problem 2 Function Data
#f(x,y) = x^4 + y^4 - 2xy + 6
def f(point):
  return (point[0] - 1)**2 + (point[1] - 333)**2 + (point[0] + point[1] - 10)^2

def fx(point):
  return 4*point[0] + 2*point[1] - 22

def fy(point):
  return 4*point[1] + 2*point[0] - 686

#p3 exclusive
def z(point):
    return point[0] + point[1] - 3

def gradf(point):
  return np.array([fx(point),fy(point)])

def grad_descent(initial,learning_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    #print(n,current_point,update_vector)
    update_vector = learning_rate*gradf(current_point)
    current_point = current_point - update_vector
  return current_point

initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 200
print('=================================================================')
print('Gradient Descent on f(x,y)')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of GD:',grad_descent(initial_guess,learning_rate,num_trials))
print('z:',z(grad_descent(initial_guess,learning_rate,num_trials)))