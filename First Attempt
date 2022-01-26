#This file is for the first attempt.

#Initialisation of the setting, buy/sell tokens, setposition (mint/burn tokens)

#What it will look like

#Initialisation

#Inputs
while True:
  try:
    l = int(input("Initial Liquidity: "))
  except ValueError:
    print("Please type a positive rational number.")
    continue
  else:
    break

while True:
  try:
    i_l_0 = int(input("Initial Lower Tick (between -70000 and 70000): "))
  except ValueError:
    print("Please type a rational number.")
    continue

  if i_l_0 < -70000:
    print("Number must be above -70000.")
    continue
  elif i_l_0 > 70000:
    print("Number must be below 70000.")
    continue
  else:
    i_l_0_ind = np.sign(i_l_0)*math.floor(abs(math.log(i_l_0)/math.log(1.0001)))+70000 #this will be the index in Tick_State
    break

while True:
  try:
    i_u_0 = int(input("Initial Upper Tick (between -70000 and 70000): "))
  except ValueError:
    print("Please type a rational number.")
    continue

  if i_u_0 < -70000:
    print("Number must be above -70000.")
    continue
  elif i_u_0 > 70000:
    print("Number must be below 70000.")
    continue
  else:
    i_u_0_ind = np.sign(i_u_0)*math.ceiling(abs(math.log(i_u_0)/math.log(1.0001)))+70000 #this will be the index in Tick_State
    break

#prepping ticks for negative numbers
if i_l_0 < i_u_0:
  pass
else:
  temp = i_l_0
  temp_ind = i_l_0_ind
  i_l_0 = i_u_0
  i_l_0_ind = i_u_0_ind
  i_u_0 = temp
  i_u_0_ind = temp_ind

p = input("Initial Price:")

L_0 = l
P_0 = p
i_0 = math.floor(math.log(P_0)/math.log(1.001)) #log(sqrt(P)) to the base of log(sqrt(1.001))

State = {[t_0,t_1] : [L_0,math.sqrt(P_0),i_0]}

Tick_State = [[0 for i in range(3)] for j in range(140002)] #assuming that token1/token0's price can be between 1/1000 to 1000, will use middle tick as 0. This requires ticks to be between -70000 and 70000
#At each tick, the 0th position holds the Tick Value, the 1st position holds LiquidityNet and the 2nd position holds LiquidityGross
Tick_State[i_l_0][0]=l
Tick_State[i_u_0][0]=-l
for i in (range(-70000,70001)):
  Tick_State[i][0] = 1.0001**i
for i in (range(i_l_0_ind,i_u_0_ind+1)):
  Tick_State[i][2]=l

User_State = {[t_0,t_1]:[0,0]}

#setposition

def setPosition(): #i_l is lower tick, i_u is upper tick
  
  #Get inputs
  while True:
    try:
      i_l = int(input("Lower Tick (between -70000 and 70000): "))
    except ValueError:
      print("Please type an integer.")
      continue

    if i_l < -70000:
      print("Number must be above -70000.")
      continue
    elif i_l > 70000:
      print("Number must be below 70000.")
      continue
    else:
      i_l_ind = np.sign(i_l)*math.floor(abs(math.log(i_l)/math.log(1.0001)))+70000 #this will be the index in Tick_State
      break

  while True:
    try:
      i_u = int(input("Upper Tick (between -70000 and 70000): "))
    except ValueError:
      print("Please type a rational number.")
      continue

    if i_u < -70000:
      print("Number must be above -70000.")
      continue
    elif i_u > 70000:
      print("Number must be below 70000.")
      continue
    else:
      i_u_ind = np.sign(i_l)*math.floor(abs(math.log(i_l)/math.log(1.0001)))+70000 #this will be the index in Tick_State
      break

  delta_L = int(input("Change in liquidity:"))
  
  #Set Values
  L = State[t_0,t_1][0]
  rt_p = State[t_0,t_1][1]
  i_c = State[t_0,t_1][2]

  #Get changes in tokens
  if i_c<i_l:
    delta_y = 0
    delta_x = delta_L*(1/math.sqrt(1.0001**i_l-1/math.sqrt(1.0001**i_u))
  elif i_c>=i_u:
    delta_y = delta_L*(math.sqrt(1.0001**i_u)-math.sqrt(1.0001**i_l))
    delta_x = 0
  else:
    delta_y = delta_L*(rt_p-math.sqrt(1.0001**i_l))
    delta_x = delta_L*(1/rt_p-1/math.sqrt(1.0001**i_u))
  
  #Prepping i_l and i_u to take care of negtative input ambiguity
  if i_l_0 < i_u_0:
    pass
  else:
    temp = i_l_0
    temp_ind = i_l_0_ind
    i_l_0 = i_u_0
    i_l_0_ind = i_u_0_ind
    i_u_0 = temp
    i_u_0_ind = temp_ind

  #Changes in States
  State[t_0,t_1][0] = L+delta_L
  Tick_State[i_l][1] = Tick_State[i_l][1] + delta_L
  Tick_State[i_u][1] = Tick_State[i_u][1] - delta_L
  for i in (range(i_l_ind,i_u_ind+1)):
    Tick_State[i][2] = Tick_State[i][2] + delta_L
  User_State[t_0,t_1][0] = User_State[t_0,t_1][0] + delta_x
  User_State[t_0,t_1][1] = User_State[t_0,t_1][1] + delta_y
  
