# TSP-Genetic
This code defines a genetic algorithm for solving the traveling salesman problem. The City and Country classes are used to represent the cities and the country, respectively. The Genetic class contains methods for initializing the population, calculating fitness, selecting parents through tournament selection, performing crossover and mutation operations, evaluating generations, finding the best generation, and showing the route of the best solution.

The fitness_function method calculates the total distance of each individual in the population and assigns a fitness value based on the distance.

The tournament_selection method selects two parents from the population based on their fitness values using a tournament selection approach.

The crossover method performs a crossover operation between two parents to create offspring.

The mutation method introduces random changes to an offspring to maintain genetic diversity in the population.

The evaluating_generation method evaluates each offspring in a generation by calculating its total distance.

The best_generation method finds the best solution in a generation based on its fitness value.

Finally, the show_route method visualizes the route of an individual using matplotlib.
