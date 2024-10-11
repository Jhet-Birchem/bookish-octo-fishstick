import numpy as np

#################################
# Problem 5
#################################
#You will have to define f, fx, and fy below

def f(point):
  return (3-point[0]*1-point[1])^2 + (7-point[0]*3-point[1])^2 + (37-point[0]*13-point[1])^2 + (331-point[0]*73-point[1])^2

def fx(point):
  return (11016*point[0] + 180*point[1] - 49336)

def fy(point):
  return (107*point[0] + 8*point[1] - 756)

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
 
initial_guess = np.array([4,40])
learning_rate = 0.0001
num_trials = 200
print('=================================================================')
print('Gradient Descent on f(a,b)')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of GD:',grad_descent(initial_guess,learning_rate,num_trials))
