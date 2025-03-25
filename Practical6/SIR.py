#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#initial values
population = 10000
beta = 0.3
gamma = 0.05
time_points = 1000

S = population - 1 
I = 1
R = 0

S_list = [S]
I_list = [I]
R_list = [R]

#calculate the new recovery and infection number first,and then calculate the number at each time
for i in range(time_points):
    new_recovery = np.random.choice(range(2),I,p=[1-gamma,gamma]).sum()
    new_infection = np.random.choice(range(2),S,p=[1-beta*(I/population),beta*(I/population)]).sum()
    
    S = max(S - new_infection,0) #S is smaller and smaller, so we need to avoid negtive number
    I = max(I - new_recovery + new_infection,0) #I is too small, so we need to avoid negtive number
    R = min(R + new_recovery,population) #R is bigger and bigger, so we need to avoid it beyond population

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize = (6,4),dpi =150)
plt.plot(S_list,label="susceptible",color="blue")
plt.plot(I_list,label="infected",color="orange")
plt.plot(R_list,label="recovered",color="green")
plt.xlabel("time")
plt.ylabel("number people")
plt.title("SIR model")
plt.legend()
plt.show()