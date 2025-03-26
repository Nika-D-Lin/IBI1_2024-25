#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#initial values
rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
population = 10000
beta = 0.3
gamma = 0.05
time_points = 1000

plt.figure(figsize=(6,4), dpi=150) #put this foreword to make sure everything put on one picture

for rate in rates: #for every rate, calculate its corresponding value
    V = population * rate #just remove the people who take vaccination
    S = max(population - V - 1,0) #if rate = 1, S will be a negtive number, so we need make sure it won't be that
    I = 1
    R = 0

    S_list = [S]
    I_list = [I]
    R_list = [R]

    for t in range(time_points):
        new_recovery = np.random.choice(range(2), int(I), p=[1-gamma, gamma]).sum()
        new_infection = np.random.choice(range(2), int(S), p=[1-beta*(I/population), beta*(I/population)]).sum()

        S = max(S - new_infection, 0)
        I = max(I - new_recovery + new_infection, 0)
        R = min(R + new_recovery, population)

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    plt.plot(I_list, label=(f"{int(rate*100)}%") if rate != 0 else "0")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()