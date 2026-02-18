import random

# -----------------------------
# Step 1: Given Probabilities
# -----------------------------

P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# -----------------------------
# Step 2: Calculate P(Free)
# Law of Total Probability
# -----------------------------

P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

# -----------------------------
# Step 3: Apply Bayes Theorem
# -----------------------------

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("----- THEORETICAL CALCULATION -----")
print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)


# ------------------------------------------------
# Step 4: Simulation to Verify (1000 Emails)
# ------------------------------------------------

emails = 1000
free_count = 0
spam_and_free = 0

for _ in range(emails):

    # Decide Spam or Ham
    if random.random() < P_spam:
        # Email is Spam
        if random.random() < P_free_given_spam:
            free_count += 1
            spam_and_free += 1
    else:
        # Email is Ham
        if random.random() < P_free_given_ham:
            free_count += 1

# Avoid division by zero
if free_count > 0:
    experimental_probability = spam_and_free / free_count
else:
    experimental_probability = 0

print("\n----- SIMULATION RESULT -----")
print("Experimental P(Spam | Free) =", experimental_probability)


