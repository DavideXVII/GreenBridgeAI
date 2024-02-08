from data_manipulator import *


def main():

    #creazione array di agricoltori
    numAgricoltori = getNumAgricoltori()
    agricoltori = []
    for agricoltore_id in range(1, numAgricoltori[0] + 1):
        nuovoagricoltore = Agricoltore(agricoltore_id)
        agricoltori.append(nuovoagricoltore)
    for agricoltore in agricoltori:
        print(f"id: {agricoltore.id}, numOrdini: {agricoltore.numOrdini}, numCertificati: {agricoltore.numCertificati}, mediaRecensioni: {agricoltore.mediaRecensioniPro}")

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