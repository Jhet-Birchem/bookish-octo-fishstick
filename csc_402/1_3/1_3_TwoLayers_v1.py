def heaviside(x):
  if x >= 0:
    return 1
  else:
    return 0
  #All in one
  #return int(x >= 0)

def sigma(x):
  return 1/(1 + 2.71828**(-x))

data = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
for d in data:
  x_0 = d[0]
  x_1 = d[1]
  x_2 = d[2]
  print('d =',d)
  #First Layer Values
  w_0_0_1 = 1 #w_start_end_layer
  w_0_1_1 = 2
  w_0_2_1 = 3
  w_1_0_1 = 4
  w_1_1_1 = 2
  w_1_2_1 = 2
  w_2_0_1 = 5
  w_2_1_1 = 1
  w_2_2_1 = 1
  b_0_1 = -2
  b_1_1 = -4
  b_2_1 = -5

  a_0_1 = heaviside(w_0_0_1*x_0 + w_1_0_1*x_1 + w_2_0_1*x_2 + b_0_1)
  a_1_1 = heaviside(w_0_1_1*x_0 + w_1_1_1*x_1 + w_2_1_1*x_2 + b_1_1)
  a_2_1 = heaviside(w_0_2_1*x_0 + w_1_2_1*x_1 + w_2_2_1*x_2 + b_2_1)
  print('a_0_1 =',a_0_1)
  print('a_1_1 =',a_1_1)
  print('a_1_1 =',a_1_1)

  #Second Layer Values
  w_0_0_2 = 3
  w_0_1_2 = 1
  w_1_0_2 = 4
  w_1_1_2 = 3
  w_2_0_2 = 6
  w_2_1_2 = 6
  b_0_2 = -2
  b_1_2 = -4

  a_0_2 = heaviside(w_0_0_2*a_0_1 + w_1_0_2*a_1_1 + w_2_0_2*a_2_1 + b_0_2)
  a_1_2 = heaviside(w_0_1_2*a_0_1 + w_1_1_2*a_1_1 + w_2_1_2*a_2_1 + b_1_2)
  print('a_0_2 =',a_0_2)
  print('a_1_2 =',a_1_2)