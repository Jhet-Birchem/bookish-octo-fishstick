def heaviside(x):
  if x >= 0:
    return 1
  else:
    return 0

data = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]

w0 = 6
w1 = 2
w2 = 2
b = -3

print('Data Point  | w.x + b \t| h(w.x + b)')
print('====================================')
for d in data:
  print(d,'  | ',w0*d[0] + w1*d[1] + w2*d[2] + b,'\t\t|',heaviside(w0*d[0] + w1*d[1] + w2*d[2] + b))