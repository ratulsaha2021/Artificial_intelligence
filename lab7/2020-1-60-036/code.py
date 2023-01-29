import random
import itertools
from scipy import special as sc

NUM_QUEENS = 8
POPULATION_SIZE = 10
MIXING_NUMBER = 2
MUTATION_RATE = 0.05


def fitness_score(seq):
    score = 0

    for row in range(NUM_QUEENS):
        col = seq[row]

        for another_row in range(NUM_QUEENS):

            if another_row== row:
                continue
            if seq[another_row] == col:
                continue
            if another_row+ seq[another_row] == row + col:
                continue
            if another_row- seq[another_row] == row - col:
                continue
            score += 1

    return score / 2


def selection(population):
    parents = []

    for j in population:
        if random.randrange(sc.comb(NUM_QUEENS, 2) * 2) < fitness_score(j):
            parents.append(j)

    return parents


def crossover(parents):
    cross_points = random.sample(range(NUM_QUEENS), MIXING_NUMBER - 1)
    offsprings = []


    permutations = list(itertools.permutations(parents, MIXING_NUMBER))

    for perm in permutations:
        offspring = []
        start_pt = 0
        for parent_idx, cross_point in enumerate(cross_points):


            parent_part = perm[parent_idx][start_pt:cross_point]
            offspring.append(parent_part)


            start_pt = cross_point

        last_parent = perm[-1]
        parent_part = last_parent[cross_point:]
        offspring.append(parent_part)
        offsprings.append(list(itertools.chain(*offspring)))

    return offsprings


def mutate(seq):
    for row in range(len(seq)):
        if random.random() < MUTATION_RATE:
            seq[row] = random.randrange(NUM_QUEENS)

    return seq


def print_found_goal(population, to_print=True):
    for j in population:
        score = fitness_score(j)
        if to_print:
            print(f'{j}. Score: {score}')
        if score == sc.comb(NUM_QUEENS, 2):
            if to_print:
                print('Solution found')
            return True

    if to_print:
        print('Solution not found')
    return False


def evolution(population):
    parents = selection(population)
    offsprings = crossover(parents)
    offsprings = list(map(mutate, offsprings))
    new_gen = offsprings

    for j in population:
        new_gen.append(j)

    new_gen = sorted(new_gen, key=lambda j: fitness_score(j), reverse=True)[:POPULATION_SIZE]

    return new_gen


def generate_population():
    population = []

    for individual in range(POPULATION_SIZE):
        new = [random.randrange(NUM_QUEENS) for idx in range(NUM_QUEENS)]
        population.append(new)

    return population


generation = 0
population = generate_population()

while not print_found_goal(population):
    print(f'Generation: {generation}')
    print_found_goal(population)
    population = evolution(population)
    generation += 1