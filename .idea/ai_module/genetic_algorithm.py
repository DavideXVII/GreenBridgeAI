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
    ids = list(range(0, numAgricoltori))  # Genera una lista di numeri da 1 a 200
    ga_data = [ids[i:i+4] for i in range(0, len(ids), 4)]
    num_genes = 4
    print(ga_data)
    # Creazione di un oggetto PyGAD per l'ottimizzazione
    ga_instance = pygad.GA(num_generations=20,
                           num_parents_mating=5,
                           fitness_func=fitness_func_wrapper(agricoltori=agricoltori),
                           sol_per_pop=100,
                           num_genes=num_genes,
                           initial_population=ga_data,
                           parent_selection_type = "sss",
                           mutation_probability=0.4, #0.3 troppo poco, 0.5 troppo
                           mutation_type = "random",
                           crossover_type="two_points",
                           keep_elitism = 1,
                           gene_type = int,
                           stop_criteria=["saturate_5"],
                           allow_duplicate_genes=False,
                           )

    # Avvio dell'ottimizzazione
    ga_instance.run()
    # Ottieni il miglior individuo dopo l'ottimizzazione
    solution, solution_fitness, solution_indices = ga_instance.best_solution()
    print("Miglior soluzioni:", solution)
    print("Fitness della migliore soluzione:", solution_fitness)
    print("solution index:", solution_indices)



if __name__ == "__main__":
    main()