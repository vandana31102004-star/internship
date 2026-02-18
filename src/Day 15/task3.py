# -----------------------------
# PART 1: Given Probabilities
# -----------------------------

P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05


# -----------------------------
# PART 2: Total Probability of "Free"
# Law of Total Probability
# -----------------------------

P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)


# -----------------------------
# PART 3: Bayes' Theorem
# -----------------------------

P_spam_given_free = (P_free_given_spam * P_spam) / P_free


# -----------------------------
# PRINT RESULTS
# -----------------------------

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)



