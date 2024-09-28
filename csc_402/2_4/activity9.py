import numpy as np

def grad_descent(initial,learning_rate,num_iterations):
  update_vector = np.array([0,0])
  current_point = np.array(initial)
  for n in range(num_iterations):
    #print(n,current_point)
    update_vector = learning_rate*gradf(current_point)
    current_point = current_point - update_vector
  return current_point

##########################################
#Problem 1 Part a - Run GD! Play with points, learning rate, and number of trials
##########################################

def f(point):
  return point[0]**3 + point[1]**3 - 3*point[0]*point[1] + 4

def fx(point):
  return 3*point[0]**2 - 3*point[1]

def fy(point):
  return 3*point[1]**2 - 3*point[0]

def gradf(point):
  return np.array([fx(point),fy(point)])

initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 50
print('=================================================================')

print('Gradient Descent on f(x,y) = x^4 + y^4 - 4xy + 1')
print('Initial Guess:',initial_guess)
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print(grad_descent(initial_guess,learning_rate,num_trials))

##########################################
#Problem 1 Part b - Run GD! Play with different starting points.
##########################################
starting_points = [[i,j] for i in range(0,5) for j in range(-1,3)]
learning_rate = 0.1
num_trials = 10
print('=================================================================')
print('Gradient Descent on f(x,y) = x^4 + y^4 - 4xy + 1')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial \t| (xn,yn)->??')
for p in starting_points:
  print(p,' \t|',grad_descent(p,learning_rate,num_trials))
  
  