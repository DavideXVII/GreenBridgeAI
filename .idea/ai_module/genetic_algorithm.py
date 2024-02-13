from data_manipulator import *
import pygad
import numpy

# Definizione della funzione di fitness
"""
def fitness_func(ga_instance, solution, solution_idx):
    MA = solution[0]
    MP = solution[1]
    NC = solution[2]
    OR = solution[3]
    fitness = (2 * OR) + (1.5 * NC) + (2 * MA) + (1.5 * MP)
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
    return batch_fitness
def main():

    #creazione array di agricoltori
    numAgricoltori = getNumAgricoltori()
    agricoltori = []
    for agricoltore_id in range (1,9): #(1, numAgricoltori[0] + 1):
        nuovoagricoltore = Agricoltore(agricoltore_id)
        agricoltori.append(nuovoagricoltore)
    for agricoltore in agricoltori:
        print(f"id: {agricoltore.id}, numOrdini: {agricoltore.numOrdini}, numCertificati: {agricoltore.numCertificati},"
              f" mediaRecensioniPro: {agricoltore.mediaRecensioniPro}, mediaRecensioniAgr: {agricoltore.mediaRecensioniAgr}")
    ga_data = []
    for agricoltore in agricoltori:
        dati = [agricoltore.numOrdini, agricoltore.numCertificati, agricoltore.mediaRecensioniAgr, agricoltore.mediaRecensioniPro]
        ga_data.append(dati)
    num_individuals = 9 #numAgricoltori[0]
    num_genes = 4
    # Creazione di un oggetto PyGAD per l'ottimizzazione
    ga_instance = pygad.GA(num_generations=20,
                           num_parents_mating=8,
                           fitness_func=fitness_func_batch,
                           fitness_batch_size=4,
                           sol_per_pop=num_individuals,
                           num_genes=num_genes,
                           initial_population=ga_data,
                           mutation_percent_genes=10,
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

"""
    ordini_agricoltore = []
    for i in range(numAgricoltori[0]):
        temp = agricoltori[i].numOrdini
        ordini_agricoltore.append(temp)
    print("numOrdini: ", ordini_agricoltore)

    certificazioni = []
    for i in range(numAgricoltori[0]):
        temp = agricoltori[i].numCertificati
        certificazioni.append(temp)
    print("certificazioni: ", certificazioni)

    media_recensioni_agr = []
    for i in range(numAgricoltori[0]):
        temp = agricoltori[i].mediaRecensioniAgr
        media_recensioni_agr.append(temp)
    print("media recensioni agricoltore: ", media_recensioni_agr)

    media_recensioni_pro = []
    for i in range(numAgricoltori[0]):
        temp = agricoltori[i].mediaRecensioniPro
        media_recensioni_pro.append(temp)
    print("media recensioni prodotti: ", media_recensioni_pro)

"""

if __name__ == "__main__":
    main()





'''

media_recensioni = np.array([4.5, 4.2, 4.8, 4.0, 3.9])
distanza_cliente = np.array([0.6, 0.7, 0.5, 0.8, 0.9])

# Define the target function (fitness function)

    def fitness_function(solution, solution_index):
        # Extract weights from the solution
        w1, w2, w3, w4 = solution

        # Calculate the fitness using the given formula
        fitness = np.sum(w1 * ordini_agricoltore +
                     w2 * certificazioni_ecosostenibili +
                     w3 * media_recensioni_agricoltore +
                     w4 * media_recensioni_prodotti)

        return fitness


# Create an instance of the pygad.GA class
ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=4,
                       fitness_func=fitness_function,
                       sol_per_pop=10,
                       num_genes=4,  # Four genes for weights w1, w2, w3, and w4
                       gene_type=float,
                       gene_space=[(-1, 1)] * 4,  # Assuming weights can be in the range [-1, 1]

                       parent_selection_type="tournament",
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=10)

# Run the genetic algorithm
ga_instance.run()

# Get the best solution found by the genetic algorithm
solution, fitness = ga_instance.output_dict['last_generation']['best_solution'], ga_instance.output_dict['last_generation']['best_solution_fitness']

# Print the result
print("Best solution (weights):", solution)
print("Fitness value:", fitness)
'''