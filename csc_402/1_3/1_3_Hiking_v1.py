def heaviside(x):
  if x >= 0:
    return 1
  else:
    return 0

def sigma(x):
  return 1/(1 + 2.71828**(-x))

data = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]

w0 = 6
w1 = 2
w2 = 2
b = -3
print('w0 =',w0,'| w1 =',w1,'| w2 =',w2,'| b =',b)

print(' ')
print('Data Point \t| w.x + b \t| h(w.x + b)')
print('====================================')
for d in data:
  print(d,'\t| ',w0*d[0] + w1*d[1] + w2*d[2] + b,'\t\t|',heaviside(w0*d[0] + w1*d[1] + w2*d[2] + b))

print(' ')
print('Data Point \t| w.x + b \t| sigma(w.x + b)')
print('====================================')
for d in data:
  print(d,'\t| ',w0*d[0] + w1*d[1] + w2*d[2] + b,'\t\t|',sigma(w0*d[0] + w1*d[1] + w2*d[2] + b))