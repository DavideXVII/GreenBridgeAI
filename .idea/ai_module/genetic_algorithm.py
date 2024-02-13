from data_manipulator import *
import pygad
import numpy

# Definizione della funzione di fitness
def fitness_func_wrapper(agricoltori):
    def fitness_func(ga_instance, solution, solution_idx):
        agr1 = agricoltori[int (solution[0])]
        agr2 = agricoltori[int (solution[1])]
        agr3 = agricoltori[int (solution[2])]
        agr4 = agricoltori[int (solution[3])]
        print(agr1, agr2, agr3, agr4)

        fitness = agr1.fitness + agr2.fitness + agr3.fitness + agr4.fitness
        return fitness

    return fitness_func

def main():

    #creazione array di agricoltori
    numAgricoltori = getNumAgricoltori()
    agricoltori = []
    for agricoltore_id in range (1, numAgricoltori + 1):
        nuovoagricoltore = Agricoltore(agricoltore_id)
        agricoltori.append(nuovoagricoltore)
    for agricoltore in agricoltori:
        print(f"id: {agricoltore.id}, fitness: {agricoltore.fitness}")
    # Creazione della popolazione iniziale
    population_size = numAgricoltori
    ga_data = []
    for _ in range(population_size):
        data = [agricoltori[i].id for i in range(4)]  # Ogni soluzione contiene 4 agricoltori
        ga_data.append(data)
    num_genes = 4
    #print(ga_data)
    # Creazione di un oggetto PyGAD per l'ottimizzazione
    ga_instance = pygad.GA(num_generations=20,
                           num_parents_mating=5,
                           fitness_func=fitness_func_wrapper(agricoltori=agricoltori),
                           sol_per_pop=population_size,
                           num_genes=num_genes,
                           initial_population=ga_data,
                           mutation_probability=0.5, #0.4 troppo poco, 0.6 troppo
                           mutation_type = "random",
                           crossover_type="single_point",
                           keep_elitism = 1
                           )

    # Avvio dell'ottimizzazione
    ga_instance.run()
    best_4_solutions, best_4_indices = ga_instance.steady_state_selection(ga_instance.last_generation_fitness,
                                                                          4)
    best_4_fitness = ga_instance.last_generation_fitness[best_4_indices]
    # Ottieni il miglior individuo dopo l'ottimizzazione
    solution, solution_fitness, solution_indices = ga_instance.best_solution()
    print("Miglior soluzioni:", solution)
    print("Fitness della migliore soluzione:", solution_fitness)
    print("solution index:", solution_indices)
    print(best_4_solutions, best_4_indices, best_4_fitness)

'''
import pygad
import numpy as np
from data_manipulator import getNumAgricoltori, Agricoltore

# Definizione della funzione di fitness
# Definizione della funzione di fitness
def fitness_func(solution, solution_idx):
    fitness = 0
    for agricoltore in solution:
        fitness += (1.5 * agricoltore.ordiniRicevuti) + (2 * agricoltore.numCertificati) + (2 * agricoltore.mediaRecensioniAgr) + (1.5 * agricoltore.mediaRecensioniPro)
    return fitness

def main():
    # Creazione array di agricoltori
    numAgricoltori = getNumAgricoltori()
    agricoltori = []
    for agricoltore_id in range(1, numAgricoltori + 1):
        nuovoagricoltore = Agricoltore(agricoltore_id)
        agricoltori.append(nuovoagricoltore)

    # Creazione della popolazione iniziale
    population_size = 10
    initial_population = []
    for _ in range(population_size):
        ga_data = [agricoltori[i] for i in range(4)]  # Ogni soluzione contiene 4 agricoltori
        initial_population.append(ga_data)

    # Creazione di un oggetto PyGAD per l'ottimizzazione
    ga_instance = pygad.GA(num_generations=20,
                           num_parents_mating=5,
                           fitness_func=fitness_func,
                           sol_per_pop=population_size,
                           num_genes=4,  # Ogni individuo ha 4 geni, uno per ogni agricoltore
                           initial_population=initial_population,
                           mutation_probability=0.5,
                           mutation_type="random",
                           crossover_type="single_point",
                           keep_elitism=1)

    # Avvio dell'ottimizzazione
    ga_instance.run()

    # Ottieni il miglior individuo dopo l'ottimizzazione
    best_solution, best_solution_fitness, _ = ga_instance.best_solution()
    print("Miglior soluzione trovata:")
    for agricoltore in best_solution:
        print(f"Agricoltore ID: {agricoltore.id}")
    print("Fitness della migliore soluzione:", best_solution_fitness)
'''

if __name__ == "__main__":
    main()