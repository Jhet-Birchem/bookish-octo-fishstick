#data = [(1,3),(3,7)]
data = [(1,3),(3,7),(13,37)]

def error_E(a):
  return sum((d[0]*a - d[1])**2 for d in data)

# ** is for exponents in python, as ^ is the exclusive or operator

print('Data Points:',data)

optimal_a = sum(d[0]*d[1] for d in data)/sum(d[0]**2 for d in data)
print('Error is Minimized when a =',optimal_a)
print('Minimum Error =',error_E(optimal_a))