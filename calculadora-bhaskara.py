import math
def baskara(a,b,c):
  delta = (b*b)-4*a*c
  if delta >= 0:
    X1= (-b+math.sqrt(delta))/(2*a)
    X2= (-b-math.sqrt(delta))/(2*a)
    return X1, X2
  else:
    return print('false')
print('Descubra os valores das raizes de uma determinada equação')
A, B, C = input('insira os valores de a, b e c respectivamente: ').split()
A = float(A)
B = float(B)
C = float(C)
Valor_raiz = baskara(A, B, C)
print(f'O valor da raiz é {Valor_raiz}')
