def heaviside(x):
  if x >= 0:
    return 1
  else:
    return 0

def sigma(x):
  return 1/(1 + 2.71828**(-x))

data = [(0,0,0,0,0),(0,0,0,0,1),(0,0,0,1,0),(0,0,0,1,1),
        (0,0,1,0,0),(0,0,1,0,1),(0,0,1,1,0),(0,0,1,1,1),
        (0,1,0,0,0),(0,1,0,0,1),(0,1,0,1,0),(0,1,0,1,1),
        (0,1,1,0,0),(0,1,1,0,1),(0,1,1,1,0),(0,1,1,1,1),
        (1,0,0,0,0),(1,0,0,0,1),(1,0,0,1,0),(1,0,0,1,1),
        (1,0,1,0,0),(1,0,1,0,1),(1,0,1,1,0),(1,0,1,1,1),
        (1,1,0,0,0),(1,1,0,0,1),(1,1,0,1,0),(1,1,0,1,1),
        (1,1,1,0,0),(1,1,1,0,1),(1,1,1,1,0),(1,1,1,1,1)]

data2 = [(0,0,0,0,0),
        (0,0,0,0,1),
        (1,1,1,0,0),
        (1,0,0,1,0),
        (1,1,0,0,0),
        (1,0,1,0,0)]

w = [30,60,50,10,90] #Change these values and rerun
b = -60 #Change this value and rerun

print('==========================================================================')
print('Weights and Bias Values')
print(f'w0 = {w[0]} | w1 = {w[1]} | w2 = {w[2]} | w3 = {w[3]} | w4 = {w[4]}| b = {b}')

print(' ')
print('Data Point  \t | w.x + b \t| h(w.x + b)')
print('========================================')
true_counter = 0
for d in data:
  print(d,' | ',sum(w[i]*d[i] for i in range(5)) + b,'\t\t|',heaviside(sum(w[i]*d[i] for i in range(5)) + b))
  #Use heaviside for Perceptrons
  #Use sigma for Sigmoid Neurons
  if heaviside(sum(w[i]*d[i] for i in range(5)) + b) == 1:
    true_counter += 1
    #For Sigmoid Neurons change == 1 to some upper bound, e.g., > 0.8
print('Number True/1/Positive?',true_counter)