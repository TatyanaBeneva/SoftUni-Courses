def distribute_the_wealth(population_list, min_wealth):
    is_distribution_possible = sum(population_list) / len(population_list) >= min_wealth

    if not is_distribution_possible:
        return "No equal distribution possible"

    distributed_list = []

    for population in population_list:
        max_wealth = max(population_list)
        index_of_max_wealth = population_list.index(max_wealth)

        if population < min_wealth:
            diff = min_wealth - population
            distributed_list.append(population + diff)
            population_list[index_of_max_wealth] -= diff
        else:
            distributed_list.append(population)

    return distributed_list

population_input = list(map(int, input().split(", ")))
minimum_wealth = int(input())

result = distribute_the_wealth(population_input, minimum_wealth)
print(result)

