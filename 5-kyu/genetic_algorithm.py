"""
🧬 Task Description: Finding a Binary String via Genetic Algorithm (GA)
This code implements a genetic algorithm (GA) to find a secret binary sequence. The task simulates the process of biological
evolution to find an optimal solution within a search space of millions of combinations. Instead of a brute-force search,
the program "grows" the solution through a succession of generations.
Key Requirements:
Representation: Each potential solution (chromosome) is a binary string. In this implementation,
integers (int) are used to speed up calculations.
Population: The algorithm must operate on a group of individuals (recommended size: 50 to 1000).
Fitness Function: The quality of a solution is evaluated based on the number of bits that do not match the target.
The final value is calculated as
1/(errors + 1), where 1.0 represents a perfect match.
Selection: Mandatory use of "Roulette Wheel Selection"—the probability of choosing a parent must be strictly proportional
to its fitness value.
Crossover: Occurs with a probability of pc=0.6. A cut is made at a random point in the chromosome, and the parts of the
two parents are swapped (single-point crossover).
Mutation: Occurs with a probability of pm=0.002. This probability must be applied individually to each bit of every
new chromosome.
Evolution Cycle: The new generation must completely replace the old one and maintain the same population size.
By default, the simulation runs for 100 iterations (generations).
Result: Upon completion of all iterations, the algorithm must return the single fittest individual found.
"""
from random import choices, random, randint
from typing import List, Tuple, Union, Callable


class GeneticAlgorithm:
    """
    A class representing a simple Genetic Algorithm using bitwise operations
    for better performance with binary string problems.
    """

    def __init__(self) -> None:
        self.population_int: List[int] = []
        self.length: int = 0

    def generate(self, length: int = 35) -> str:
        """
        Generates a random chromosome, stores its integer value and
        returns its binary string representation.
        """
        chrom_int = randint(0, (2 ** length) - 1)
        self.population_int.append(chrom_int)
        return bin(chrom_int)[2:].zfill(length)

    @staticmethod
    def select(population: List[int], fitnesses: List[float]) -> List[int]:
        """
        Performs Roulette Wheel Selection to pick two parent chromosomes.
        """
        return choices(population, fitnesses, k=2)

    def mutate(self, chromosome: int, p_m: float) -> int:
        """
        Applies bitwise mutation by generating a random mask
        based on the mutation probability.
        """
        mask = 0
        for _ in range(self.length - 1):
            # Roll dice for each bit and shift the mask
            mask = (mask + (random() <= p_m)) << 1

        # Add the last bit and XOR to flip mutated bits
        return (mask + (random() <= p_m)) ^ chromosome

    def crossover(self, chromosomes: List[int], p_c: float) -> Union[Tuple[int, int], List[int]]:
        """
        Performs a single-point bitwise crossover between two chromosomes.
        """
        if random() > p_c:
            return chromosomes

        # Pick a random split point
        left_part: int = randint(1, self.length - 1)
        right_part: int = self.length - left_part

        parent_a, parent_b = chromosomes

        # Create a mask for the right part (bits to the right of the split)
        mask = (1 << right_part) - 1

        # Combine the shifted head of one parent with the masked tail of the other
        child_ab = ((parent_a >> right_part) << right_part) | (parent_b & mask)
        child_ba = ((parent_b >> right_part) << right_part) | (parent_a & mask)

        return child_ab, child_ba

    def run(self,
            fitness: Callable[[str], float],
            length: int,
            p_c: float,
            p_m: float,
            iterations: int = 100) -> str:
        """
        Main evolutionary loop to find the optimal binary string.
        """
        self.length = length
        self.population_int = []

        # Determine population size based on the chromosome complexity
        pop_size = (60, 90, 180)[sum((length > 34, length > 63))]

        # Initialize population
        population_str: List[str] = [self.generate(length) for _ in range(pop_size)]

        for _ in range(iterations):
            new_population_int: List[int] = []
            # Calculate fitness for the current population once per generation
            current_fitnesses: List[float] = list(map(fitness, population_str))

            # Evolution step: Selection, Crossover, and Mutation
            for _ in range(pop_size // 2):
                parents = self.select(self.population_int, current_fitnesses)
                offspring = self.crossover(parents, p_c)

                mutated_0 = self.mutate(offspring[0], p_m)
                mutated_1 = self.mutate(offspring[1], p_m)

                new_population_int.extend((mutated_0, mutated_1))

            # Update population for the next generation
            self.population_int = new_population_int
            population_str = [bin(x)[2:].zfill(self.length) for x in self.population_int]

        # Return the chromosome with the highest fitness found in the last generation
        return max(population_str, key=fitness)


# ==================== TESTS ====================

if __name__ == '__main__':

    import time
    from typing import Callable


    # Assuming the GeneticAlgorithm class is already defined above

    def get_fitness_factory(goal: str) -> Callable[[str], float]:
        """
        Creates a fitness function that calculates the inverse of
        the Hamming distance to the goal string.
        """

        def fitness(chromosome: str) -> float:
            score = sum(1 for a, b in zip(chromosome, goal) if a != b)
            return 1 / (score + 1)

        return fitness


    def run_test_case(ga: GeneticAlgorithm,
                      goal: str,
                      p_c: float = 0.6,
                      p_m: float = 0.002,
                      iterations: int = 100) -> None:
        """
        Runs a single test case, measures performance, and prints results.
        """
        length = len(goal)
        fitness_fn = get_fitness_factory(goal)

        print(f"Testing {length}-bit goal...")

        start_time = time.time()
        result = ga.run(fitness_fn, length, p_c, p_m, iterations)
        end_time = time.time()

        duration = end_time - start_time
        is_correct = result == goal

        print(f"  Result:  {'PASSED' if is_correct else 'FAILED'}")
        print(f"  Time:    {duration:.4f} seconds")
        if not is_correct:
            print(f"  Target: {goal}")
            print(f"  Found:  {result}")
        print("-" * 40)


    def run_all_tests():
        """
        Organized test suite for different complexity levels.
        """
        ga = GeneticAlgorithm()

        print("=== STARTING GENETIC ALGORITHM TESTS ===\n")

        # Test 1: Short 16-bit goal
        short_goal = "1110110111101101"
        run_test_case(ga, short_goal)

        # Test 2: Standard 35-bit goal (from the original task)
        std_goal = "11110110111011011011101101111011011"
        run_test_case(ga, std_goal, iterations=100)

        # Test 3: Longer 64-bit goal
        long_goal = "1110110111101101111011011110110111101101111011011110110111101101"
        run_test_case(ga, long_goal)

        print("=== ALL TESTS COMPLETED ===")

    run_all_tests()
