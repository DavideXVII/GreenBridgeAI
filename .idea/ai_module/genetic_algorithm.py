from data_manipulator import *
import pygad
import numpy

# Definizione della funzione di fitness

def fitness_func(ga_instance, solution, solution_idx):
    MA = solution[0]
    MP = solution[1]
    NC = solution[2]
    OR = solution[3]
    fitness = (1.5 * OR) + (2 * NC) + (2 * MA) + (1.5 * MP)
    return fitness
"""

def fitness_func_batch(ga_instance, solutions, solutions_indices):
    global number_of_calls
    batch_fitness = []
    for solution in solutions:
        MA = solution[0]
        MP = solution[1]
        NC = solution[2]
        OR = solution[3]
        fitness = (2 * OR) + (1.5 * NC) + (2 * MA) + (1.5 * MP)
        batch_fitness.append(fitness)
    return batch_fitness"""
def main():

    #creazione array di agricoltori
    numAgricoltori = getNumAgricoltori()
    agricoltori = []
    for agricoltore_id in range (1, numAgricoltori[0] + 1):
        nuovoagricoltore = Agricoltore(agricoltore_id)
        agricoltori.append(nuovoagricoltore)
    for agricoltore in agricoltori:
        print(f"id: {agricoltore.id}, numOrdini: {agricoltore.numOrdini}, numCertificati: {agricoltore.numCertificati},"
              f" mediaRecensioniPro: {agricoltore.mediaRecensioniPro}, mediaRecensioniAgr: {agricoltore.mediaRecensioniAgr}")
    ga_data = []
    for agricoltore in agricoltori:
        dati = [agricoltore.numOrdini, agricoltore.numCertificati, agricoltore.mediaRecensioniAgr, agricoltore.mediaRecensioniPro]
        ga_data.append(dati)
    num_individuals = numAgricoltori[0]
    num_genes = 4
    # Creazione di un oggetto PyGAD per l'ottimizzazione
    ga_instance = pygad.GA(num_generations=20,
                           num_parents_mating=5,
                           fitness_func=fitness_func,
                           sol_per_pop=num_individuals,
                           num_genes=num_genes,
                           initial_population=ga_data,
                           mutation_probability=0.5, #0.4 troppo poco, 0.6 troppo
                           mutation_type = "random",
                           crossover_type="single_point",
                           keep_elitism = 1,

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

