import random
import matplotlib.pyplot as plt
import numpy as np
import math
class City(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Country(object):
    def __init__(self,cities):
        self.cities=cities
class Genetic:
    def __init__(self,individual):
        self.individual=individual
        self.population=[]
        for i in range(len(self.individual)):
            self.population.append(np.random.permutation(list(range(0,len(self.individual)))))
        self.population_fitness={}
        self.generation=[]
        self.evaluate_generations=[]
        self.generation_fitness={}  
    def fitness_function(self):
        fitness=[]
        distance=[]
        for i in range(len(self.population)):
            for j in range(len(self.population[i])-1):
                xDis = abs((self.individual[self.population[i][j]-1].x)-(self.individual[self.population[i][j+1]-1].x))
                yDis = abs((self.individual[self.population[i][j]-1].y)-(self.individual[self.population[i][j+1]-1].y))
                distance.append(round(np.sqrt((xDis ** 2) + (yDis ** 2)),2))
            sum_distance=sum(distance)
            fitness.append(sum_distance)
        for num in range(len(self.population)):
            self.population_fitness.update({num:fitness[num]})
        return self.population_fitness
    def tournament_selection(self):
        parents = random.choices(self.population_fitness, k=10)
        parents = sorted(parents)
        for key,value in self.population_fitness.items():
            if value==parents[0]:
                first_parent=key
            if value==parents[1]:
                second_parent=key
        return first_parent,second_parent
    def crossover(self,first_parent,second_parent):
        offspring=[]
        crossover_point1=random.randint(0,(int(len(self.individual)/2)))
        crossover_point2=random.randint(int(len(self.individual)/2),(len(self.individual)-1))
        for individual in range(len(self.population[first_parent])):
            if individual<crossover_point1:
                offspring.append(self.population[first_parent][individual])
            elif crossover_point1<=individual and individual<crossover_point2:
                offspring.append(self.population[second_parent][individual])
            elif crossover_point2<individual:
                offspring.append(self.population[first_parent][individual])
        return offspring
    def mutation(self,offspring):
        i=np.random.randint(2,(len(offspring)-1))
        j=np.random.randint(2,(len(offspring)-1))
        t=offspring[i]
        offspring[i]=offspring[j]
        offspring[j]=t
        return offspring
    def evaluating_generation(self,offspring):
        distance=[]
        for  i in range(len(offspring)-1):
            xDis = abs((self.individual[offspring[i]].x)-(self.individual[offspring[i+1]].x))
            yDis = abs((self.individual[offspring[i]].y)-(self.individual[offspring[i+1]].y))
            distance.append(round(np.sqrt((xDis ** 2) + (yDis ** 2)),2))
        self.generation.append(offspring)
        self.evaluate_generations.append(sum(distance))          
    def best_genration(self):
        for i in range(len(self.generation)):
            self.generation_fitness.update({i:self.evaluate_generations[i]})     
        best=min(self.generation_fitness.values())
        for i,j in self.generation_fitness.items():
            if j==best:
                return self.generation[i]
    def show_route(self,mutation_offspring):
        x=[]
        y=[]
        colors = []
        for entity in mutation_offspring:
            x.append(self.individual[entity].x)
            y.append(self.individual[entity].y)
            colors.append('#%06X' % random.randint(0, 0xFFFFFF))
        for i in range(len(x) - 1):
            plt.plot([x[i], x[i+1]], [y[i], y[i+1]], '-o', color=colors[i])  
        plt.show()      
##########################Cycle####################################################Cycle##########################    
number_of_city=int(input('Enter number of city:'))
x1,x2=input('Specify the beginning and end of the x range:').split()
y1,y2=input('Specify the beginning and end of the y range:').split()        
cities=[]
for i in range(number_of_city):
    x=random.randint(int(x1),int(x2))
    y=random.randint(int(y1),int(y2))
    city=City(x,y)
    cities.append(city)
usa=Country(cities)
a=Genetic(usa.cities)
a.fitness_function()
crossover_Condition=True
while crossover_Condition:
    first_parent,second_parent=a.tournament_selection()
    offspring=a.crossover(first_parent,second_parent)
    setoffspring=set(offspring)
    if len(setoffspring)==len(offspring):
        crossover_Condition=False
        offspring.append(offspring[0])
    else:
        crossover_Condition=True
for i in range(0,5):
    mutation_offspring=a.mutation(offspring)
    a.evaluating_generation(mutation_offspring)
    offspring=mutation_offspring
a.show_route(a.best_genration())








