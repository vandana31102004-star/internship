import random

# Number of simulations
trials = 10000

print("----- INDEPENDENT EVENTS (Coin + Die) -----")

# Theoretical Probability
p_heads = 1/2
p_six = 1/6
theoretical_independent = p_heads * p_six
print("Theoretical Probability (Heads AND 6):", theoretical_independent)

# Simulation
count_independent = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)
    
    if coin == "H" and die == 6:
        count_independent += 1

experimental_independent = count_independent / trials
print("Experimental Probability:", experimental_independent)


print("\n----- DEPENDENT EVENTS (Marbles Without Replacement) -----")

# Theoretical Probability
p_first_red = 5/10
p_second_red = 4/9
theoretical_dependent = p_first_red * p_second_red
print("Theoretical Probability (Both Red):", theoretical_dependent)

# Simulation
count_dependent = 0

for _ in range(trials):
    bag = ["R"]*5 + ["B"]*5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)
    
    if first == "R" and second == "R":
        count_dependent += 1

experimental_dependent = count_dependent / trials
print("Experimental Probability:", experimental_dependent)
