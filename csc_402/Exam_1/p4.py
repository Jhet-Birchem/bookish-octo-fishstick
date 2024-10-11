import numpy as np

#################################
# Problem 4 - System!
#################################
A = np.array([[1,2],[3,4]])
y = np.array([1,2])
A_inv = np.linalg.inv(A)
print('A^-1 =\n', A_inv)
x = np.matmul(A_inv,y)
print('x =',x)

#################################
# Problem 4 - GD
#################################
#f(x,y,y) = (8x + 6y + 7z - 5)^2 + (3x + 0y + 9z - 3)^2 + (1x + 3y + 3z - 7)^2
#
#You will have to define f, fx, fy, AND fz below

def f(point):
  return (8*point[0] + 6*point[1] + 7*point[2] - 5)^2 + (3*point[0] + 0*point[1] + 9*point[2] - 3)^2 + (1*point[0] + 3*point[1] + 3*point[2] - 7)^2

def fx(point):
  return 2*(74*point[0] + 51*point[1] + 86*point[2] - 56)

def fy(point):
  return 6*(17*point[0] + 15*point[1] + 17*point[2] - 17)

def fz(point):
  return 2*(86*point[0] + 51*point[1] + 139*point[2] - 83)

def gradf(point):
  return np.array([fx(point),fy(point),fz(point)])
 
def grad_descent(initial,learning_rate,num_iterations):
    update_vector = np.array([0,0,0])
    current_point = np.array(initial)
    for n in range(num_iterations):
        #print(n,current_point,update_vector)
        update_vector = learning_rate*gradf(current_point)
        current_point = current_point - update_vector
        return current_point
 
initial_guess = np.array([-2.5,-3.5,-1.5])
learning_rate = 0.001
num_trials = 200
print('=================================================================')
print('Gradient Descent on f(x,y,z)')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of GD:',grad_descent(initial_guess,learning_rate,num_trials))
