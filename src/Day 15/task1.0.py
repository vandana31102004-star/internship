import random

# ----------------------------
# PART 1: Sample Space
# ----------------------------

actions = ["Click", "Scroll", "Exit"]

sample_space = []

for first_action in actions:
    for second_action in actions:
        sample_space.append((first_action, second_action))

total_outcomes = len(sample_space)

# ----------------------------
# PART 2: Event (At least one Click)
# ----------------------------

event_click = []

for outcome in sample_space:
    if "Click" in outcome:
        event_click.append(outcome)

probability_click = len(event_click) / total_outcomes

# ----------------------------
# PART 3: Dice Simulation
# ----------------------------

trials = 1000
count_sum_7 = 0

for i in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials
