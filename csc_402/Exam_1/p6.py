import numpy as np

#Problem 6 Function Data
#f(x,y) = x^4 + y^4 - 2xy + 6
def f(point):
    return point[0]**4 + point[1]**4 - 2*point[0]*point[1] + 6

def fx(point):
    return 4*point[0]**3 - 2*point[1]

def fy(point):
    return 4*point[1]**3 - 2*point[0]

def gradf(point):
    return np.array([fx(point),fy(point)])

def gradf_squares(point):
    #Returns vector (f_x**2,f_y**2) at point = (x,y)
    return np.array([fx(point)**2,fy(point)**2])

def gradf_pow_p(point,p):
    #Returns vector (|f_x|**p,|f_y|**p) at point = (x,y)
    return np.array([abs(fx(point))**p,abs(fy(point))**p])
 
starting_points = [[i,j] for i in range(1,5) for j in range(-2,3)]
 
##########################################################
#
# Standard GD
#
##########################################################

def grad_descent(initial,learning_rate,num_iterations):
    update_vector = np.array([0,0])
    current_point = np.array(initial)
    for n in range(num_iterations):
        #print(n,current_point,update_vector)
        update_vector = learning_rate*gradf(current_point)
        current_point = current_point - update_vector
    return current_point

initial_guess = np.array([1,2])
learning_rate = 0.01
num_trials = 500
print('=================================================================')
print('Gradient Descent on f(x,y)')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of GD:',grad_descent(initial_guess,learning_rate,num_trials))

print('Multiple Starting Points!')
for initial in starting_points:
    print(initial,' \t|',grad_descent(initial,learning_rate,num_trials))
print('=================================================================')

##########################################################
#
# Adagrad (This one is done for you)
#
##########################################################

def adagrad(initial,learning_rate,num_iterations,eps):
    update_vector = np.array([0,0])
    Gn = np.array([0,0])
    current_point = np.array(initial)
    for n in range(num_iterations):
        Gn = Gn + gradf_squares(current_point)
        Gn_matrix = np.array([[1/np.sqrt(Gn[0] + eps),0],[0,1/np.sqrt(Gn[1] + eps)]])
        update_vector = learning_rate*np.matmul(Gn_matrix,gradf(current_point))
        current_point = current_point - update_vector
    return current_point
 
initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 500
epsilon = 0.1
print('=================================================================')
print('Adagrad on f(x,y)')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of Adagrad:',adagrad(initial_guess,learning_rate,num_trials,epsilon))

print('Multiple Starting Points!')
for initial in starting_points:
    print(initial,' \t|',adagrad(initial,learning_rate,num_trials,epsilon))
print('=================================================================')

##########################################################
#
# Adadelta!
#
##########################################################
def adadelta(initial,learning_rate,num_iterations,eps,alpha):
    update_vector = np.array([0,0])
    EGn = np.array([0,0])
    current_point = np.array(initial)
    for n in range(num_iterations):
        #print(n,current_point)
        EGn = (alpha * EGn) + ((1 - alpha) * gradf_squares(current_point))
        EGn_matrix = np.array([[1/np.sqrt(EGn[0] + eps),0],[0,1/np.sqrt(EGn[1] + eps)]])
        update_vector = learning_rate*np.matmul(EGn_matrix,gradf(current_point))
        current_point = current_point - update_vector
    return current_point
 
initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 500
epsilon = 0.01
alpha = 0.9
print('=================================================================')
print('Adadelta on f(x,y)')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of Adadelta:',adadelta(initial_guess,learning_rate,num_trials,epsilon,alpha))

print('Multiple Starting Points!')
for initial in starting_points:
    print(initial,' \t|',adadelta(initial,learning_rate,num_trials,epsilon,alpha))
print('=================================================================')

##########################################################
#
# ADAM!
#
##########################################################
def adam(initial,learning_rate,num_iterations,eps,alpha1,alpha2):
    update_vector = np.array([0,0])
    EG1 = np.array([0,0])
    EG2 = np.array([0,0])
    current_point = np.array(initial)
    for n in range(num_iterations):
        EG1 = (alpha1 * EG1) + ((1 - alpha1) * gradf(current_point))
        EG2 = (alpha2 * EG2) + ((1 - alpha2) * gradf_squares(current_point))
        EG1_hat = EG1 / (1 - alpha1**(n+1))
        EG2_hat = EG2 / (1 - alpha2**(n+1))
        Gn_matrix = np.array([[1/np.sqrt(EG2_hat[0] + eps),0],[0,1/np.sqrt(EG2_hat[1] + eps)]])
        update_vector = learning_rate*np.matmul(Gn_matrix,EG1_hat)
        current_point = current_point - update_vector
    return current_point
 
initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 500
epsilon = 0.1
alpha1 = 0.8
alpha2 = 0.9
print('=================================================================')
print('ADAM on f(x,y)')
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of ADAM:',adam(initial_guess,learning_rate,num_trials,epsilon,alpha1,alpha2))

print('Multiple Starting Points!')
for initial in starting_points:
    print(initial,' \t|',adam(initial,learning_rate,num_trials,epsilon,alpha1,alpha2))
print('=================================================================')

##########################################################
#
# AdaMax! (p=1)
#
##########################################################
def adamax(initial,learning_rate,num_iterations,eps,alpha1,alpha2,p):
    update_vector = np.array([0,0])
    EG1 = np.array([0,0])
    EGP = np.array([0,0])
    current_point = np.array(initial)
    for n in range(num_iterations):
        EG1 = (alpha1 * EG1) + ((1 - alpha1) * gradf(current_point))
        EGP = (alpha2 * EGP) + ((1 - alpha2) * gradf_pow_p(current_point,p))
        EG1_hat = EG1 / (1 - alpha1**(n+1))
        EGP_hat = EGP / (1 - alpha2**(n+1))
        Gn_matrix = np.array([[1/np.sqrt(EGP_hat[0] + eps),0],[0,1/np.sqrt(EGP_hat[1] + eps)]])
        update_vector = learning_rate*np.matmul(Gn_matrix,EG1_hat)
        current_point = current_point - update_vector
    return current_point
 
initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 500
epsilon = 0.1
alpha1 = 0.8
alpha2 = 0.9
p = 1
print('=================================================================')
print('AdaMax on f(x,y)')
print('Power of p:',p)
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of AdaMax:',adamax(initial_guess,learning_rate,num_trials,epsilon,alpha1,alpha2,p))

print('Multiple Starting Points!')
for initial in starting_points:
    print(initial,' \t|',adamax(initial,learning_rate,num_trials,epsilon,alpha1,alpha2,p))
print('=================================================================')

##########################################################
#
# AdaMax! (p=3)
#
##########################################################

initial_guess = np.array([4,2])
learning_rate = 0.01
num_trials = 500
epsilon = 0.1
alpha1 = 0.8
alpha2 = 0.9
p = 3
print('=================================================================')
print('AdaMax on f(x,y)')
print('Power of p:',p)
print('Learning Rate:',learning_rate)
print('Number of Iterations:', num_trials)
print('Initial Guess:',initial_guess)
print('Output of AdaMax:',adamax(initial_guess,learning_rate,num_trials,epsilon,alpha1,alpha2,p))

print('Multiple Starting Points!')
for initial in starting_points:
    print(initial,' \t|',adamax(initial,learning_rate,num_trials,epsilon,alpha1,alpha2,p))
print('=================================================================')

