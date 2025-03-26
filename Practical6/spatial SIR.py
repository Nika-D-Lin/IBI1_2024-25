#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

beta = 0.3
gamma = 0.05
time_points = 100

population = np.zeros((100,100)) #set a 100*100 area
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1 #infected poeple
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Population Status')
plt.show()

for t in range(time_points):
    new_population = population.copy()  #copy the current state

    for x in range(100):
        for y in range(100):
            if population[x, y] == 1:  #infected people
                for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]: #infect surround 8 people
                    X = x + dx
                    Y = y + dy
                    if 0 <= X < 100 and 0 <= Y < 100: #avoid value beyond the range
                        if population[X, Y] == 0 and np.random.choice(range(100))/100 <= beta:
                            new_population[X, Y] = 1  
            
                if np.random.choice(range(100))/100 <= gamma: #infected ones may recover
                    new_population[x, y] = 2

    population = new_population

    if t in [9,49,99]: #only shoe the picture at time 10,50,100
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.colorbar(label='Population Status')
        plt.title(f"Time {t+1}")
        plt.show()