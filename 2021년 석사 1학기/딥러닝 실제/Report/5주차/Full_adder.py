import numpy as np

def AND(x1,x2):             # AND 게이트
  x = np.array([x1,x2])       # 입력
  w = np.array([0.5,0.5])   # 가중치
  b = -0.7                  # 편향
  tmp = np.sum(x*w) + b     # 임시저장변수tmp
  if tmp <= 0:
    return 0
  else:
    return 1
  
def OR(x1,x2):              # OR 게이트              
  x = np.array([x1,x2])     # 입력
  w = np.array([0.5,0.5])   # 가중치
  b = -0.2                  # 편향
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def NAND(x1,x2):
  x = np.array([x1,x2])
  w = np.array([-0.5,-0.5])
  b = 0.7
  tmp = np.sum(w*x)+b
  if tmp <= 0:
    return 0
  else:
    return 1

# Exclusive or
# (A+B)*(A'*B')
def XOR(x1,x2):
  s1 = NAND(x1,x2)
  s2 = OR(x1,x2)
  y = AND(s1,s2)
  return y

# Full Adder
# SUM = (A XOR B) XOR Cin
# Cout =  Cin AND (X XOR B) OR A AND B
def Full_adder(x1,x2,c1):
  s = XOR(x1,x2)      #SUM
  sum = XOR(c1,s)

  a = XOR(x1,x2)    #Carry
  b = AND(c1,a)
  c = AND(x1,x2)
  cout = OR(b,c)

  print(' x1 = {0}, x2 = {1}, c = {2} Cout = {3} sum = {4}'.format(x1,x2,c1,cout,sum ))

for x in range(0,8):
    x1,x2,c = input('x1 x2 c1 을 입력하시오!\n').split()
    x1 = int(x1)
    x2 = int(x2)
    c = int(c)
    if((x1<2)&(x2<2)&(c<2)):
        Full_adder(x1,x2,c)
    else:
        print('입력값을 확인하세요')